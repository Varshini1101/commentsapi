from django.conf.urls import url
from core import views

urlpatterns =[
    url(r'^api/core$',views.core_list),
   
]