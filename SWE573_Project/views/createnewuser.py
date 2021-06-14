from django.shortcuts import render, redirect
from account.forms import creationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate #bunlar kayıt olduğu an login olsun diye kullanılıyor
from django.contrib.auth.decorators import login_required


def createnewuser(request):
    if request.method == 'POST':
        form = creationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = creationForm()
    return render(request, 'pages/createaccount.html', context={
        'form': form
    })