from django.shortcuts import render, redirect #response icin render ve yönlendirme için form yollandıktan sonra redirect
from SWE573_Project.forms import ReportForm #html olarak forms kısmında olusturduğumuz formu buraya import ediyoruz 
from SWE573_Project.models import ReportModel

def report(request):
    form = ReportForm() #form initialize edildi
    if request.method == 'POST': #formun validasyonu burada yapılıyor
        form = ReportForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            article = request.article
            form.save(user_id=user_id, article = article)
            return redirect('homepage')
        

    context = {
        'form' : form #form gönderebilmek için devamı template kısmında yapılacak
    }
    return render(request, 'pages/report.html', context=context)
    
    
    #HttpResponse('<h1>merhaba</1>') #pathe gelirlerse cevap dönmek icin olusutrulan 
    #fonksiyon bunları view dosyalarına yazcaz ardindan bu config icindeki urlden cagirilir
