# Generated by Django 4.0.2 on 2022-03-06 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_review_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book_id',
            new_name='movie_id',
        ),
    ]