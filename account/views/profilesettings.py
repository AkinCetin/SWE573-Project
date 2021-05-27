from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfileSettingsForm

@login_required(login_url='/')
def profilesettings(request):
    if request.method == 'POST':
        form = ProfileSettingsForm(request.POST,request.FILES, instance = request.user) #request.FILE çıkardım eklenebilir 
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful')
    else:
        form = ProfileSettingsForm(instance = request.user)
    return render(request, 'pages/profilesettings.html', context={
        'form': form
    })