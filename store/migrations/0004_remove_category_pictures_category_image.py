# Generated by Django 4.2 on 2023-07-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_image_category_pictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pictures',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='categories/'),
        ),
    ]
