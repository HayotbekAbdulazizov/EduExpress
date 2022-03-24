# Generated by Django 4.0.3 on 2022-03-23 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_university_slug_universitytranslation_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='slug',
        ),
        migrations.AddField(
            model_name='universitytranslation',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
