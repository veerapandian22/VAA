# Generated by Django 4.2.6 on 2023-10-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn_code', models.CharField(max_length=5, unique=True)),
                ('product_code', models.CharField(max_length=4, unique=True)),
                ('product_name', models.CharField(max_length=30)),
                ('product_img_path', models.CharField(max_length=30)),
                ('product_desc', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('stack_qty', models.IntegerField()),
                ('available_qty', models.IntegerField()),
                ('manufacturer_from', models.CharField(max_length=30)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
