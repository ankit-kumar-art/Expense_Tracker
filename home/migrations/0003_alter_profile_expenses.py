# Generated by Django 5.1.3 on 2024-11-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_user_profile_user_profile_expenses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]
