# Generated by Django 2.1.7 on 2019-03-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='image',
            field=models.ImageField(default='', upload_to='flowers_images', verbose_name='Фотография'),
        ),
    ]
