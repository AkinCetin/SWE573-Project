from django.shortcuts import render, get_object_or_404
from SWE573_Project.models import ArticleModel
import logging

logger = logging.getLogger('article_read_by')


def details(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    logger.info('article read:' + request.user.username)
    return render(request, 'pages/details.html', context={
        'article': article,
    })