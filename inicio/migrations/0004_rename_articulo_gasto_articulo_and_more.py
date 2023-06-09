# Generated by Django 4.1.7 on 2023-04-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_gasto_articulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gasto',
            old_name='articulo',
            new_name='Articulo',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='cantidad',
            new_name='Cantidad',
        ),
        migrations.AddField(
            model_name='gasto',
            name='Precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
