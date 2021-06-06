from django import forms #form oluşturabilmek için form adında bir folder oluşturup init vb eklendikten sonra iletisimi olusturduk
#kullanıcıdan almak istediğimiz bilgileri burada field olarak belirleyeceğiz
from SWE573_Project.models import TagModel

class TagForm(forms.ModelForm): #gelen formun validasyonu viewde yapılıyor
    url = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = TagModel
        exclude = ['user',]

    def save(self, commit=True, **kwargs):
        m = super(TagForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.user_id = kwargs.get('user_id')
            m.save()
        return m