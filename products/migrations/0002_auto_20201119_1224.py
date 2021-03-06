# Generated by Django 3.1.3 on 2020-11-19 12:24

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('available', 'Disponível'), ('unavailable', 'Indisponível'), ('deleted', 'Deletado')], default=products.models.Products.update_status, max_length=20),
        ),
    ]
