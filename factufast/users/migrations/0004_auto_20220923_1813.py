# Generated by Django 3.2.15 on 2022-09-23 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20220923_1804"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="client_address",
            new_name="address",
        ),
        migrations.RenameField(
            model_name="client",
            old_name="client_logo",
            new_name="logo",
        ),
        migrations.RenameField(
            model_name="client",
            old_name="client_name",
            new_name="name",
        ),
    ]
