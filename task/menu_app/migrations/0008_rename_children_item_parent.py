# Generated by Django 4.1.5 on 2023-01-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0007_alter_item_children'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='children',
            new_name='parent',
        ),
    ]
