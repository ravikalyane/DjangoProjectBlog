# Generated by Django 3.0.5 on 2020-05-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_about_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about_article',
            field=models.CharField(default='', max_length=300, unique=True),
        ),
    ]
