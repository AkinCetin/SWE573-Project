# Generated by Django 3.2.2 on 2021-05-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWE573_Project', '0003_remove_articlemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
