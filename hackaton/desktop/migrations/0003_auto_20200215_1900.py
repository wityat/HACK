# Generated by Django 3.0.3 on 2020-02-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0002_auto_20200215_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='session_key',
            field=models.CharField(max_length=200, verbose_name='session_key'),
        ),
    ]
