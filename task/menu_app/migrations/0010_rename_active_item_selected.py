# Generated by Django 4.1.5 on 2023-01-10 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0009_item_active_alter_item_uri'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='active',
            new_name='selected',
        ),
    ]