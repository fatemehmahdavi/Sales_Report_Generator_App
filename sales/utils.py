#all helper functions
import base64,uuid #UUID, Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids. 
from customers.models import Customer
from profiles.models import Profile
import matplotlib as plt
import seaborn as sns
from io import BytesIO  # BytesIO is a method that manipulate bytes data in memory.
#First we need to create a file-like object with the use of BytesIO and matplotlib and use base64 encode and decode method on our file-like objects
def generate_code():
    code=uuid.uuid4() #uuid4() creates a random UUID.
    code_mod=str(code).replace('-','').upper()[:12]
    return code_mod

def get_salesman_from_id(val):
    salesman=Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer=Customer.objects.get(id=val)
    return customer.user.username

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png') #create plot with the use of BYTESIO object as a file-like object
    buffer.seek(0)                    #seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file. 
    image_png=buffer.getvalue()       #retrieve the content of the file
    graph=base64.b64decode(image_png) #encode the bytes-like object(image_png) and get the encoded bytes
    graph=graph.decode('utf-8')       #to get string out of bytes we use decoding 
    buffer.close()                    #free the buffer memory
    return graph

def get_key(res_by):
    if res_by=='#1':
        key='transaction_id'
    elif res_by=='#2':
        key='created'
    return key

def get_chart(chart_type,data,results_by,**kwargs):
    plt.switch_backedn('AGG')  #switch the backend,in matplotlib is a tool responsible for drawing plots.in jupyter notebook we use the inline backend but for web app we use AGG and it renders PNGs
    fig=plt.figure(figsize(10,4)) #size of charts
    key=get_key(results_by)
    d=data.groupby(key)['total_price'].agg('sum')

    if chart_type=='#1':
        print('bar chart')
        sns.barplot(x=key,y='total_price',data=d)
        #plt.bar(d[key],data['total_price'])
    elif chart_type=='#2':
        print('pie chart')
        #labels=kwargs.get('label')
        plt.pie(data=d,x='total_price',labels=d[key].values)
    elif chart_type=='#3':
        print('line chart')
        plt.plot(d[key],d['total_price'],color='green',marker='o')
    else:
        print('failed to identify the chart type')

    plt.tight_layout() #subplot(s) fits in to the figure area
    chart=get_graph()
    return chart
