# Generated by Django 4.2 on 2023-07-06 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='pictures',
        ),
    ]