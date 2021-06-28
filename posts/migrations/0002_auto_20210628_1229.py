# Generated by Django 3.0 on 2021-06-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='content_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='content_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='content_no',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='slug_de',
            field=models.SlugField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='slug_en',
            field=models.SlugField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='slug_no',
            field=models.SlugField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_de',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_no',
            field=models.CharField(max_length=30, null=True),
        ),
    ]