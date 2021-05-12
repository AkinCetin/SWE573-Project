from django.db import models
from autoslug import AutoSlugField

class TagModel(models.Model):
    name = models.CharField(max_length=30 ,blank=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table = 'tags'