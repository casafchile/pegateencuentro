# Generated by Django 3.2 on 2021-05-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210501_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='tag',
        ),
        migrations.AddField(
            model_name='trabajo',
            name='tag',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
