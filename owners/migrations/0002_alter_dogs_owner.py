# Generated by Django 4.0.4 on 2022-05-10 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner1', to='owners.owner'),
        ),
    ]
