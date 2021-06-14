from django.shortcuts import render, redirect 
from SWE573_Project.forms import ReportForm 
from SWE573_Project.models import ReportModel
from SWE573_Project.models import ArticleModel
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def report(request, article_id):
    form = ReportForm() 
    if request.method == 'POST': 
        form = ReportForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            form.save(user_id=user_id, article_id = article_id)
            article = ArticleModel.objects.get(id = article_id)
            return redirect('details', article.slug)
        

    context = {
        'form' : form 
    }
    return render(request, 'pages/report.html', context=context)
    
    