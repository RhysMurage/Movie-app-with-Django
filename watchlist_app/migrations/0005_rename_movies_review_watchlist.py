# Generated by Django 3.2 on 2021-07-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movies',
            new_name='watchlist',
        ),
    ]
