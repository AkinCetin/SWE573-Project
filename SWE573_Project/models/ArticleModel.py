from django.db import models
from autoslug import AutoSlugField
from SWE573_Project.models import TagModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ArticleModel (models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    authors = models.CharField(max_length=150)
    publish_date = models.DateTimeField(auto_now_add=True) #pubmed tarihini çekmek araştırılacak
    update_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    tags = models.ManyToManyField(TagModel, related_name='article')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name= 'article')

    class Meta:
        db_table = 'articles'
        verbose_name='Article'
        verbose_name_plural='Articles'

    def __str__(self):
        return self.title




