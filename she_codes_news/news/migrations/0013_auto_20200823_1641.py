# Generated by Django 3.0.8 on 2020-08-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200823_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='author',
            field=models.CharField(max_length=200, verbose_name='written by'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.CharField(default='Type of Story', max_length=20, verbose_name='story category'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='content',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(default='placeholder-1.jpg', upload_to='story/images/', verbose_name='story photo'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='linkedin_url',
            field=models.CharField(default='Paste your LinkedIn URL here', max_length=200, verbose_name='linkedIn profile URL'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='title',
            field=models.CharField(max_length=200, verbose_name='story title'),
        ),
    ]