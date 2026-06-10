
from django.urls import path
from .views import login, staff_create,logout,show_user
urlpatterns = [
    path('login/', login, name='login'),
    path('staff/', staff_create, name='staff_create'),
    path('show_user/', show_user, name='show_user'),
    path('logout/', logout, name='logout'),  
]