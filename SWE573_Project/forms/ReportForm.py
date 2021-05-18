from django.forms import ModelForm #form oluşturabilmek için form adında bir folder oluşturup init vb eklendikten sonra iletisimi olusturduk
#kullanıcıdan almak istediğimiz bilgileri burada field olarak belirleyeceğiz
from SWE573_Project.models import ReportModel

class ReportForm(ModelForm): #gelen formun validasyonu viewde yapılıyor
    class Meta:
        model = ReportModel
        exclude = ['user', 'article']

    def save(self, commit=True, **kwargs):
        m = super(ReportForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.user_id = kwargs.get('user_id')
            m.article_id = kwargs.get('article_id')
            m.save()
        return m