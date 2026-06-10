from django.shortcuts import render
from django.contrib.auth.hashers import make_password

def base(request):
    print(make_password("Ujjwal"))
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'dashboard.html')



