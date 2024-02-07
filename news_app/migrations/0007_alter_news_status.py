# Generated by Django 4.0 on 2024-02-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_rename_image_news_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('DF', 'DRAFT'), ('PB', 'PUBLISHED')], default='PB', max_length=2),
        ),
    ]