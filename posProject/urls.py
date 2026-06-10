
from django.contrib import admin
from django.urls import path
from django.urls import include
from posProject.views import base, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authApp.urls')),
    path('base/', base,name='base'),
    path('dashboard/', dashboard,name='dashboard')
]

