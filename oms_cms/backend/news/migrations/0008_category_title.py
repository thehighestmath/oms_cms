# Generated by Django 2.2.5 on 2019-12-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20191209_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, default='', max_length=350, verbose_name='Заголовок'),
        ),
    ]
