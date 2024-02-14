# Generated by Django 5.0.1 on 2024-02-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0042_alter_book_ratings_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='Book.category'),
        ),
    ]