# Generated by Django 5.0.1 on 2024-02-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_alter_book_average_rating_alter_book_isbn10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(null=True),
        ),
    ]