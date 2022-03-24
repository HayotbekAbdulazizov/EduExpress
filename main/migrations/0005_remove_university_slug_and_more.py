# Generated by Django 4.0.3 on 2022-03-23 20:18

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_postimage_postimagetranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='faculties',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='grands',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='image',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='universitytranslation',
            name='world_rating',
        ),
        migrations.AlterField(
            model_name='universitytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slug', to='main.university'),
        ),
    ]
