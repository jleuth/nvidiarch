# Generated by Django 5.1.3 on 2024-12-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
