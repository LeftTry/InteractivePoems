# Generated by Django 2.2.3 on 2019-07-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='name',
            field=models.TextField(default='name'),
            preserve_default=False,
        ),
    ]
