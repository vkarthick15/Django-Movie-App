# Generated by Django 4.0.2 on 2022-03-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
