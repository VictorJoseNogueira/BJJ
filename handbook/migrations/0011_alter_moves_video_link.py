# Generated by Django 5.0.6 on 2024-06-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0010_alter_moves_author_alter_moves_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='Video_link',
            field=models.URLField(),
        ),
    ]
