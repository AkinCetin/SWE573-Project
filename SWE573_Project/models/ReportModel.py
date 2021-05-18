from django.db import models

class ReportModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank= False, null=False)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Reports'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return self.email()
