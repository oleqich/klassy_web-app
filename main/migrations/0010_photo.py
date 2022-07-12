# Generated by Django 4.0.5 on 2022-07-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_dishesmodel_description_alter_dishesmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
    ]
