from django.contrib.auth import login
from django.shortcuts import redirect

def loginView(request):
    login(request)
    return redirect('homepage')
