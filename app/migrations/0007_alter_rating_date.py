# Generated by Django 5.1.3 on 2024-12-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rating_distro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='date',
            field=models.DateField(help_text='Date when the rating was given', verbose_name='Date of Rating'),
        ),
    ]