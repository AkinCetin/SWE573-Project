from django.shortcuts import render
from SWE573_Project.models import ArticleModel
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def mainpage(request):
    search = request.GET.get('search')
    articles = ArticleModel.objects.order_by('-id')
    if search:
        articles = articles.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search) |
            Q(keywords__icontains=search)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)
    
    
    return render(request, 'pages/homepage.html', context={
        'articles': paginator.get_page(page)
    })