# Generated by Django 2.2.5 on 2019-09-25 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_register_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_Name',
            new_name='User_Email',
        ),
    ]