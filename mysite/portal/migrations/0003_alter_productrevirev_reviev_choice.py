# Generated by Django 4.1.7 on 2023-10-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrevirev',
            name='reviev_choice',
            field=models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='5'),
        ),
    ]
