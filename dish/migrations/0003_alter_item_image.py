# Generated by Django 4.0.5 on 2022-06-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaqI3_h5Q1yNKrlIJN6nEgROw3PlkeN4wd1Ac2E9Z645VZg1DpMj5SCYm2DNgU2foWbtM&usqp=CAU', max_length=500),
        ),
    ]