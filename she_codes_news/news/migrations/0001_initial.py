# Generated by Django 3.0.8 on 2020-08-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='story title')),
                ('author', models.CharField(max_length=50, verbose_name='written by')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('category', models.CharField(default='Type of Story', max_length=20, verbose_name='story category')),
                ('content', models.TextField(verbose_name='')),
                ('linkedin_url', models.CharField(blank=True, default='Paste your LinkedIn URL here', max_length=200, verbose_name='linkedIn profile URL')),
                ('image', models.ImageField(default='placeholder-1.jpg', upload_to='story_image/', verbose_name='story photo')),
            ],
        ),
    ]
