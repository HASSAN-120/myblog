# Generated by Django 4.2 on 2023-08-07 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
