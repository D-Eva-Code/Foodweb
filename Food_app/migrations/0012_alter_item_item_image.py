# Generated by Django 5.1.2 on 2024-12-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_app', '0011_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_image',
            field=models.TextField(default='data:image/jpeg;base64,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'),
        ),
    ]