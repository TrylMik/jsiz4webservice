# Generated by Django 4.0.5 on 2022-06-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment_post_delete_item_delete_todolist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
