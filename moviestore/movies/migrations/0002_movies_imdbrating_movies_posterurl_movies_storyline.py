# Generated by Django 4.0.2 on 2022-02-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='imdbRating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='posterurl',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='storyline',
            field=models.TextField(null=True),
        ),
    ]
