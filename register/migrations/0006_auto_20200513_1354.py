# Generated by Django 3.0.5 on 2020-05-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200513_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='presence',
            field=models.CharField(choices=[('Виступали', 'True'), ('Не виступали', 'False')], default='Не виступали', max_length=15, verbose_name='Виступав на конференції'),
        ),
    ]
