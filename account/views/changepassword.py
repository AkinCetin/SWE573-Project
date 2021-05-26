from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.save()
            messages.success(request, 'Password changed successfully')
            update_session_auth_hash(request, new_password)
            return redirect('changepassword')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pages/changepassword.html', context={
        'form': form
    })