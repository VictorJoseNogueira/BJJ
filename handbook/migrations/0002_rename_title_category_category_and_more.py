# Generated by Django 5.0.6 on 2024-06-16 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='difficulty',
            old_name='title',
            new_name='difficulty',
        ),
    ]
