# Generated by Django 3.2 on 2021-05-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210501_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='payment',
            field=models.IntegerField(null=True),
        ),
    ]
