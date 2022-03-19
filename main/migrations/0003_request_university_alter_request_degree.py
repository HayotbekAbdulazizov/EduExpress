# Generated by Django 4.0.3 on 2022-03-18 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_degree_degreetranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.university'),
        ),
        migrations.AlterField(
            model_name='request',
            name='degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.degree'),
        ),
    ]
