# Generated by Django 4.0.3 on 2022-03-17 21:17

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=300, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone Number')),
                ('additional', models.TextField(blank=True, verbose_name='Additional Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='universities', to='main.country')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UniversityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.university')),
            ],
            options={
                'verbose_name': 'UniversityImage',
                'verbose_name_plural': 'UniversityImages',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UniversityTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('rating', models.CharField(blank=True, max_length=100, verbose_name='Rating')),
                ('world_rating', models.CharField(blank=True, max_length=100, verbose_name='World Rating')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('faculties', models.TextField(blank=True, verbose_name='Faculties')),
                ('grands', models.TextField(blank=True, verbose_name='Grands')),
                ('image', models.ImageField(blank=True, upload_to='university_images/', verbose_name='Image')),
                ('description', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.university')),
            ],
            options={
                'verbose_name': 'University Translation',
                'db_table': 'main_university_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master'), ('slug', 'language_code')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UniversityImageTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('image', models.ImageField(upload_to='university_images/', verbose_name='University image')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.universityimage')),
            ],
            options={
                'verbose_name': 'UniversityImage Translation',
                'db_table': 'main_universityimage_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CountryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(blank=True, upload_to='country_images/', verbose_name='Image')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.country')),
            ],
            options={
                'verbose_name': 'Country Translation',
                'db_table': 'main_country_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]