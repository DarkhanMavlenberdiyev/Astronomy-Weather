
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='main'),
    path('del/<str:name>/',views.delete_city,name='delete_city'),
    path('check/',views.check_city,name='check')
]
