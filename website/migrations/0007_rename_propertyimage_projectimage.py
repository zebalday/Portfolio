# Generated by Django 4.2.10 on 2024-02-22 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_user_is_public_project_is_public'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PropertyImage',
            new_name='ProjectImage',
        ),
    ]
