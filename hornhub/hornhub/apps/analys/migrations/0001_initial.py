# Generated by Django 2.2.6 on 2019-10-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_analys', models.TextField(verbose_name='текст для анализа')),
            ],
            options={
                'verbose_name': 'анализ',
                'verbose_name_plural': 'анализа',
            },
        ),
    ]
