# Generated by Django 2.2.6 on 2019-10-01 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nome',
            old_name='Nome',
            new_name='nome',
        ),
    ]
