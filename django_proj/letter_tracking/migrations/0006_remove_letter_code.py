# Generated by Django 3.0.7 on 2020-07-30 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0005_auto_20200730_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='code',
        ),
    ]