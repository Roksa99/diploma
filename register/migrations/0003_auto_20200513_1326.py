# Generated by Django 3.0.5 on 2020-05-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200512_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='presence',
            field=models.BooleanField(choices=[(True, 'Виступали'), (False, 'Не виступали')], default=False, verbose_name='Виступав на конференції'),
        ),
    ]
