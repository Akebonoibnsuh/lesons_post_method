# Generated by Django 5.0.6 on 2024-06-29 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(help_text='Рекомендованная розничная цена', validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)], verbose_name='Цена')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
        ),
    ]
