# Generated by Django 4.2.10 on 2024-02-29 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_certification_libraries_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='framework',
            new_name='frameworks',
        ),
    ]
