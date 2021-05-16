from django.shortcuts import render, get_object_or_404
from SWE573_Project.models import ArticleModel, TagModel
from django.core.paginator import Paginator


def tag(request, tagSlug):
    tag = get_object_or_404(TagModel, slug=TagModel)
    articles = TagModel.article.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)
    return render(request, 'pages/mainpage.html', context={
        'articles': paginator.get_page(page)
    })