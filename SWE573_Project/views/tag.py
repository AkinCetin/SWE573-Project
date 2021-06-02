from django.shortcuts import render, redirect
from SWE573_Project.models import ArticleModel
from SWE573_Project.forms import TagForm
from django.core.paginator import Paginator

def tag(request, article_id):
    form = TagForm() 
    if request.method == 'POST': 
        form = TagForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            form.save(user_id=user_id, article_id = article_id)
            article = ArticleModel.objects.get(id = article_id)
            return redirect('details', article.slug)
        

    context = {
        'form' : form 
    }
    return render(request, 'pages/tag.html', context=context)

    
    
