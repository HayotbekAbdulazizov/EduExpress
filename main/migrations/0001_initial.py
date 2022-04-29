# Generated by Django 4.0.3 on 2022-04-29 18:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(blank=True, max_length=200, verbose_name='Surname')),
                ('age', models.CharField(max_length=10, verbose_name='Age')),
                ('country', models.CharField(blank=True, max_length=300, verbose_name='Country')),
                ('lang_certificate', models.BooleanField(blank=True, default=False, verbose_name='Language Certificate')),
                ('score', models.FloatField(blank=True, default=0, null=True, verbose_name='Score')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('additional', models.TextField(blank=True, verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'ClientRequest',
                'verbose_name_plural': 'ClientRequest',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('slug_en', models.SlugField(null=True, verbose_name='Slug')),
                ('slug_uz', models.SlugField(null=True, verbose_name='Slug')),
                ('slug_ru', models.SlugField(null=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, upload_to='country_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Creator',
                'verbose_name_plural': 'Creators',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, verbose_name='Title')),
                ('title_en', models.CharField(blank=True, max_length=400, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(blank=True, max_length=400, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(blank=True, max_length=400, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='*')),
                ('slug_en', models.SlugField(blank=True, null=True, unique=True, verbose_name='*')),
                ('slug_uz', models.SlugField(blank=True, null=True, unique=True, verbose_name='*')),
                ('slug_ru', models.SlugField(blank=True, null=True, unique=True, verbose_name='*')),
                ('image', models.ImageField(blank=True, upload_to='news_images/', verbose_name='Image Cover')),
                ('image_en', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Image Cover')),
                ('image_uz', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Image Cover')),
                ('image_ru', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Image Cover')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_uz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('date_en', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date')),
                ('date_uz', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date')),
                ('date_ru', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('slug_en', models.SlugField(null=True, verbose_name='Slug')),
                ('slug_uz', models.SlugField(null=True, verbose_name='Slug')),
                ('slug_ru', models.SlugField(null=True, verbose_name='Slug')),
                ('rating', models.CharField(blank=True, max_length=100, verbose_name='Rating')),
                ('rating_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rating')),
                ('rating_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rating')),
                ('rating_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rating')),
                ('world_rating', models.CharField(blank=True, max_length=100, verbose_name='World Rating')),
                ('world_rating_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='World Rating')),
                ('world_rating_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='World Rating')),
                ('world_rating_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='World Rating')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('location_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('location_uz', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('location_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='university_images/', verbose_name='Image')),
                ('image_en', models.ImageField(blank=True, null=True, upload_to='university_images/', verbose_name='Image')),
                ('image_uz', models.ImageField(blank=True, null=True, upload_to='university_images/', verbose_name='Image')),
                ('image_ru', models.ImageField(blank=True, null=True, upload_to='university_images/', verbose_name='Image')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='main.country')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.program')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.clientrequest')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.university')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.degree'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='main.language'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='main.program'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.university'),
        ),
    ]
