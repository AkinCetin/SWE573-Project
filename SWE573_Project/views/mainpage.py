from django.shortcuts import render
from SWE573_Project.models import ArticleModel
from django.core.paginator import Paginator


def mainpage(request):
    articles = ArticleModel.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)
    return render(request, 'pages/mainpage.html', context={
        'articles': paginator.get_page(page)
    })