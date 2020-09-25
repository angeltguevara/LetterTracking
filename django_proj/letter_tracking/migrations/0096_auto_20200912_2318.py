# Generated by Django 3.1 on 2020-09-12 23:18

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0095_letter_destinatario'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='caucus',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'N/a')], default='N/a', max_length=100),
        ),
        migrations.AddField(
            model_name='letter',
            name='cosigners',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'N/a')], default='None', max_length=1000, verbose_name='Cosigner(s)'),
        ),
    ]
