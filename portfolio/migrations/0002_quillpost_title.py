# Generated by Django 3.1.6 on 2021-05-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quillpost',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]