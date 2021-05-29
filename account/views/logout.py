from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutView(request):
    logout(request)
    return redirect('login')