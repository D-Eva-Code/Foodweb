# Generated by Django 5.1.2 on 2024-12-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_app', '0010_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_image',
            field=models.ImageField(default='foods.jpg', upload_to='foodfolder'),
        ),
    ]
