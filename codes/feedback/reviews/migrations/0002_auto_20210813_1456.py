# Generated by Django 3.2.5 on 2021-08-13 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='feedback',
            new_name='review_text',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='username',
            new_name='user_name',
        ),
    ]
