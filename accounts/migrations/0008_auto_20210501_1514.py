# Generated by Django 3.2 on 2021-05-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210501_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajo',
            name='tag',
        ),
        migrations.AddField(
            model_name='empresa',
            name='tag',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]