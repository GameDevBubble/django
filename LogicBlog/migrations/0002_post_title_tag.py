# Generated by Django 4.1.1 on 2022-09-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogicBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='#logicodenet', max_length=255),
        ),
    ]
