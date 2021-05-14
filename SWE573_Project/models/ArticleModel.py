from django.db import models
from autoslug import AutoSlugField
from SWE573_Project.models import TagModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from datetime import datetime

class ArticleModel (models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    authors = models.CharField(max_length=255)
    pmid = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True) #pubmed tarihini çekmek araştırılacak
    update_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(null=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    tags = models.ManyToManyField(TagModel, related_name='article')

    class Meta:
        db_table = 'articles'
        verbose_name='Article'
        verbose_name_plural='Articles'

    def __str__(self):
        return self.title




