# Generated by Django 3.0.8 on 2020-08-18 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
