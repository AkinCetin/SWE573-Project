from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def contact(request):
    context = {
        'key': 'baslik'
    }
    return render(request, 'pages/contacts.html', context=context)