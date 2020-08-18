# Generated by Django 3.1 on 2020-08-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0024_remove_letter_partido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Caucus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caucus_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Legislature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legislature_name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specific_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_topic_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='letter',
            name='notice',
            field=models.CharField(default='N/a', max_length=9, verbose_name='If a notice was sent, specify the number'),
        ),
    ]