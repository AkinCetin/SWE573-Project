from django.db import models

class ReportModel(models.Model):
    user = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE ,related_name= 'reports', null=True)
    article = models.ForeignKey('SWE573_Project.ArticleModel', on_delete=models.CASCADE, related_name= 'reports', null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Reports'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


