# Generated by Django 4.0.6 on 2024-06-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0008_director_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='directores'),
        ),
    ]
