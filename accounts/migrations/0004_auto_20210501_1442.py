# Generated by Django 3.2 on 2021-05-01 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.estudiante'),
        ),
        migrations.AddField(
            model_name='estado',
            name='trabajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.trabajo'),
        ),
    ]
