# Generated by Django 3.1 on 2020-08-17 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0018_auto_20200817_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='action',
            new_name='acción',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='notice_num',
            new_name='notice',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='comments',
            new_name='observaciones',
        ),
    ]