from django.shortcuts import render


def mainpage(request):
    return render(request, 'pages/mainpage.html', context={})