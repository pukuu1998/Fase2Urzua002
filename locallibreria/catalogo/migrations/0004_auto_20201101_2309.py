# Generated by Django 3.1.2 on 2020-11-02 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20201101_2244'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieInstance',
            new_name='MovieStatus',
        ),
    ]