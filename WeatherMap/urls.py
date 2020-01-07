
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign/',include("signmenu.urls")),
    path('weather/', include('weather.urls')),
    path('',include('weather.urls')),
    path('astronomy/',include('mars.urls')),
    path('epic/',include('epic.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns+=staticfiles_urlpatterns()
