# Generated by Django 4.0.5 on 2022-07-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_dishesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishesmodel',
            name='tab',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=9, verbose_name='Tab'),
        ),
    ]