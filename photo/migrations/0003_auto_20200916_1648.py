# Generated by Django 3.1.1 on 2020-09-16 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]
