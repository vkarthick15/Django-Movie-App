# Generated by Django 4.0.2 on 2022-03-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='duration',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='releaseDate',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='year',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
