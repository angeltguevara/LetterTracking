# Generated by Django 3.1 on 2020-08-17 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0021_auto_20200817_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='cosigners',
            new_name='legislatura',
        ),
    ]