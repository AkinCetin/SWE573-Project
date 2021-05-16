from django.shortcuts import render
from SWE573_Project.models import ArticleModel


def mainpage(request):
    articles = ArticleModel.objects.all()
    return render(request, 'pages/mainpage.html', context={
        'articles': articles
    })