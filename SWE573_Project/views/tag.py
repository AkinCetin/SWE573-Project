from django.shortcuts import render, redirect
from SWE573_Project.models import ArticleModel, TagModel
from SWE573_Project.forms import TagForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def tag(request, article_id):
    form = TagForm() 
    if request.method == 'POST': 
        form = TagForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            cleaned_info = form.cleaned_data
            i = TagModel.objects.filter(name = cleaned_info['name'])
            if not i.exists():
                i = form.save(user_id=user_id, article_id = article_id)
            else:
                i = i.first()
            article = ArticleModel.objects.get(id = article_id)
            article.tags.add(i)
            return redirect('details', article.slug)
        

    context = {
        'form' : form 
    }
    return render(request, 'pages/tag.html', context=context)

    
    
