# Generated by Django 3.1.7 on 2021-03-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20210309_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimages',
            name='filter_class',
        ),
        migrations.AddField(
            model_name='project',
            name='filter_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
