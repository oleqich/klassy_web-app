# Generated by Django 4.0.5 on 2022-07-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_dishesmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishesmodel',
            name='description',
            field=models.CharField(max_length=70, verbose_name='Desription'),
        ),
        migrations.AlterField(
            model_name='dishesmodel',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Name of the dish'),
        ),
    ]
