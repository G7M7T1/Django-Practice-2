# Generated by Django 4.0.6 on 2022-07-29 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='text',
            new_name='message',
        ),
    ]
