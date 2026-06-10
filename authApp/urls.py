
from django.urls import path
from .views import login, staff_create
urlpatterns = [
    path('login/', login, name='login'),
    path('staff/', staff_create, name='staff_create'),
    
]