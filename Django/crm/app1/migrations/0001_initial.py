# Generated by Django 2.2.5 on 2019-09-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crse', models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]