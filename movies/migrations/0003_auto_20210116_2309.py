# Generated by Django 3.1.5 on 2021-01-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210116_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='actor',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_en',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Гасло'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_ru',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Гасло'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='movieshots',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва'),
        ),
    ]
