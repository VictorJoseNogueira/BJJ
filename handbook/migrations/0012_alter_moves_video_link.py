# Generated by Django 5.0.6 on 2024-06-18 02:40

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0011_alter_moves_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='Video_link',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
