# Generated by Django 5.0.6 on 2024-07-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0009_alter_director_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('direccion', models.CharField(default='', max_length=150)),
                ('telefono', models.CharField(default='', max_length=150)),
            ],
        ),
    ]