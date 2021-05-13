from django.db import models

class ContactModel(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    class Meta(self):
        db_table = 'Contacts'
        verbose_name = 'Contact'
        verbose_name_plural= 'Contacts'


