from django.db import models

class ContactModel(models.Model):
    db_table = 'Contacts'
    verbose_name = 'Contact'
    verbose_name_plural= 'Contacts'


