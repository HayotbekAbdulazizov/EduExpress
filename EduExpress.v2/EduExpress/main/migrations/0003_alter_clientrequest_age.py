# Generated by Django 3.2.3 on 2022-04-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220429_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='age',
            field=models.CharField(blank=True, max_length=10, verbose_name='Age'),
        ),
    ]