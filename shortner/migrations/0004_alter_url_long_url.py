# Generated by Django 3.2.7 on 2021-09-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_alter_url_long_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.TextField(),
        ),
    ]