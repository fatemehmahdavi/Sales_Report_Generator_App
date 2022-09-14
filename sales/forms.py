from django import forms

CHART_CHOICES=(
    ('#1','Bar chart'),
    ('#2','Pie chart'),
    ('#3','Line chart'),

)

RESULT_CHOICES=(
    ('#1','transaction'),
    ('#2','sales_date'),

)

class SalesSearchFrom(forms.Form):  #create a custom form that is not related to any of the models
    #https://docs.djangoproject.com/en/4.1/topics/forms/
    #https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
    date_from=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type=forms.ChoiceField(choices=CHART_CHOICES)
    results_by=forms.ChoiceField(choices=RESULT_CHOICES)