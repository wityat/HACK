# Generated by Django 3.0.3 on 2020-02-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0004_remove_siteuser_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='session_key',
            field=models.CharField(default=0, max_length=200, verbose_name='session_key'),
            preserve_default=False,
        ),
    ]
