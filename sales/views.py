from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'sales/main.html',{}) # {} refers to what we want to pass to the template