# Generated by Django 5.1.4 on 2025-01-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_entries_member_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='entries',
            field=models.IntegerField(default=0),
        ),
    ]
