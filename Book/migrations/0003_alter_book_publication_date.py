# Generated by Django 5.0.1 on 2024-02-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_book_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]