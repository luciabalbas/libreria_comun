# Generated by Django 5.2.1 on 2025-05-11 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'Género', 'verbose_name_plural': 'Géneros'},
        ),
    ]
