from django.shortcuts import render, get_object_or_404
from SWE573_Project.models import ArticleModel
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login")
def details(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    return render(request, 'pages/details.html', context={
        'article': article,
    })