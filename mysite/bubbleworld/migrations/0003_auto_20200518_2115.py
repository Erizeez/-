# Generated by Django 3.0.6 on 2020-05-18 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bubbleworld', '0002_remove_user_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='black_list',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follow_to',
        ),
    ]
