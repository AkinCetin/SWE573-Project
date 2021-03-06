# Generated by Django 3.2.2 on 2021-06-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWE573_Project', '0003_alter_articlemodel_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='authors',
            field=models.CharField(max_length=556),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='keywords',
            field=models.CharField(max_length=558),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='pmid',
            field=models.CharField(max_length=557, unique=True),
        ),
    ]
