# Generated by Django 3.0.8 on 2020-08-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200819_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(default='placeholder-1.jpg', upload_to='static/news/images'),
        ),
    ]
