# Generated by Django 2.2.6 on 2019-10-06 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комменты'},
        ),
        migrations.AlterModelOptions(
            name='stat',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]