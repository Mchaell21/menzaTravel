# Generated by Django 5.0.6 on 2024-07-19 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logAuth', '0015_alter_post_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='thumbnail',
        ),
    ]
