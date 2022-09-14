from django import forms
from .models import Report

#https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
#widget gets rendered on the view

class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=('name','remarks')