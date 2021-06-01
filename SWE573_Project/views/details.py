from django.shortcuts import render, get_object_or_404
from SWE573_Project.models import ArticleModel



def details(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    return render(request, 'pages/details.html', context={
        'article': article,
    })