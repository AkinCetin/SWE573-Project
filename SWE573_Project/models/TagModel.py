from django.db import models
from autoslug import AutoSlugField

class TagModel(models.Model):
    name = models.CharField(max_length=30 ,blank=False)
    slug = AutoSlugField(populate_from='name', unique=True)
    user = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE ,related_name= 'tags', null=True)


    class Meta:
        db_table = 'tags'
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'

    def __str__(self):
        return self.name
