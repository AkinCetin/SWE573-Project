# Generated by Django 3.2.2 on 2021-06-02 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SWE573_Project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='SWE573_Project.articlemodel'),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=models.ManyToManyField(related_name='article', to='SWE573_Project.TagModel'),
        ),
    ]