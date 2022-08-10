# Generated by Django 4.0.6 on 2022-08-06 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acnt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="Title of the Cuisine, Like 'North Indian', 'South Indian'.", max_length=150, unique=True)),
                ('details', models.TextField(blank=True, help_text='Enter the details.', max_length=3000)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the Dish Category.', max_length=150, unique=True)),
                ('details', models.TextField(blank=True, help_text='Enter the details.', max_length=3000)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenuId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('menu_type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner')], help_text='Select menu type.', max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_menu_id', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_menu_id', to='acnt.vendorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(help_text='Price.', null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_menu', to='core_app.dish')),
                ('vendor_menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_menu', to='core_app.vendormenuid')),
            ],
        ),
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="Title of the Dish Category, like 'Idli', 'Dosa'.", max_length=150, unique=True)),
                ('details', models.TextField(blank=True, help_text='Enter the details.', max_length=3000)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_category', to='core_app.cuisine')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to='core_app.dishcategory'),
        ),
        migrations.CreateModel(
            name='CustomerMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('menu_type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner')], help_text='Select menu type.', max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_menu', to=settings.AUTH_USER_MODEL)),
                ('vendor_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_menu', to='core_app.vendormenu')),
            ],
        ),
    ]