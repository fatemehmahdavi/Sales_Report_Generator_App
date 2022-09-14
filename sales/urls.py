from importlib.resources import path
from django.urls import path
from .views import (
    SaleDetailView,
    home_view,
    SalesListView,
    SaleDetailView,

)

urlpatterns = [
    #urlpatterns for class_based views
    path('list/',SalesListView.as_view(),name='list'), #Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-based views have an as_view() class method which returns a function that can be called when a request arrives for a URL matching the associated pattern. 
    path('detail/<pk>',SaleDetailView.as_view(),name='detail'), #pk refers to which object should be displayed in detailview
    #urlpatterns for function_based views
    path('list/',home_view,name='home'),
    # path('list/',sale_list_view,name='list'),
    # path('detail/<pk>',sale_detail_view,name='detail'),



    
    
]