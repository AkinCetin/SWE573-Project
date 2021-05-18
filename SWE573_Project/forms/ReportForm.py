from django import forms #form oluşturabilmek için form adında bir folder oluşturup init vb eklendikten sonra iletisimi olusturduk
#kullanıcıdan almak istediğimiz bilgileri burada field olarak belirleyeceğiz


class ReportForm(forms.Form): #gelen formun validasyonu viewde yapılıyor
    email = forms.EmailField(label= 'Email', max_length=255,) #sayfadaki ismi burdaki değişkenden alır istenirse label eklenebilir
    isim_soyisim = forms.CharField(max_length=255)
    mesaj = forms.CharField(widget=forms.Textarea) #bunu bir text areaya çevirmek için widget kullanıyoruz