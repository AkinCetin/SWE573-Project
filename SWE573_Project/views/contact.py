from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    context = {
        'key': 'baslik'
    }
    return render(request, 'pages/contacts.html', context=context)