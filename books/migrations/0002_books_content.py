# Generated by Django 5.0.7 on 2024-07-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='content',
            field=models.TextField(default='Python 0 дан 100 гача'),
            preserve_default=False,
        ),
    ]
