from http.client import CREATED
from venv import create
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
#from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import SalesSearchFrom
import pandas as pd
from .utils import get_customer_from_id,get_salesman_from_id,get_chart
from reports.forms import ReportForm
# Create your views here.
def home_view(request):
    search_form=SalesSearchFrom(request.POST or None)
    report_form=ReportForm() #send the data with ajax
    chart=None
    sales_df=None
    positions_df=None
    merged_df=None
    no_data=None
    
    if request.method=='POST':
        date_from=request.POST.get('date_from')
        date_to=request.POST.get('date_to')
        chart_type=request.POST.get('chart_type')  
        results_by=request.POST.get('results_by')
        sale_qs=Sale.objects.filter(created__date__lte=date_to,created__date__gte=date_from)
        if len(sale_qs)>0: #if we have a queryset(if we have sales objects created) between the date from and date to we'll create a dataframe
            sales_df=pd.DataFrame(sale_qs.values())

            #show customername and salesman name instead of their id
            sales_df['customer_id']=sales_df['customer_id'].apply(get_customer_from_id) #The apply() method allows you to apply a function along one of the axis of the DataFrame, default 0, which is the index (row) axis.
            sales_df['salesman_id']=sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df['created']=sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))

            sales_df=sales_df.rename({'customer_id':'customer','salesman_id':'salesman','id':'sales_id'},axis=1) #axis=1 refers to column, rename the column names
            #sales_df['salles_id']=sales_df['id'] add a column to the data frame
            
            positions_data=[] #we cannot use qs.get_positions for querysets to get the objects so we use a list and for loop
            for sale in sale_qs:
                for position in sale.get_position():
                    obj={
                        'position_id':position.id,
                        'product':position.product.name,
                        'quantitiy':position.quantitity,
                        'price':position.price,
                        'sales_id':position.get_sales_id(),
                    }
                    positions_data.append(obj)
            positions_df=pd.DataFrame(positions_data)
            merged_df=pd.DataFrame(sales_df,positions_df,on='sales_id')

            sales_df=sales_df.to_html()         #Render a DataFrame as an HTML table
            positions_df=positions_df.to_html()
            merged_df=merged_df.to_html()
            df=df.to_html()

            df=merged_df.groupby('trsnsaction_id')['price'].agg('sum')
            chart=get_chart(chart_type,sales_df,results_by)  #data is the dataframe(df)

        else:
            no_data="No data is available in this date range"

    context={
        'search_form':search_form,
        'sales_df':sales_df,
        'positions_df':positions_df,
        'merged_df':merged_df,
        'df':df,
        'chart':chart,
        'report_form':report_form,
        'no_data':no_data,
        }
    return render(request,'sales/home.html',context) # {} refers to what we want to pass to the template

#class_based views   
class SalesListView(LoginRequiredMixin,ListView): #When using class-based views, you can achieve the same behavior as with login_required by using the LoginRequiredMixin. This mixin should be at the leftmost position in the inheritance list.
    model=Sale
    template_name='sales/main.html'

class SaleDetailView(LoginRequiredMixin,DetailView):
    model=Sale
    template_name='sales/detail.html'

#function_based views
'''
def sale_list_view(request):
    qs=Sale.objects.all() #https://stackoverflow.com/questions/22804252/django-orm-objects-filter-vs-objects-all-filter-which-one-is-preferre 
    return render(request,'sales/main.html',{'object_list':qs})

def sale_detail_view(request,**kwargs):
    pk=kwargs.get('pk') #https://docs.djangoproject.com/en/4.1/topics/db/queries/ , #https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
    obj=get_object_or_404(Sale,pk=pk)
    return render(request,'sales/detail.html',{'object':obj})

'''