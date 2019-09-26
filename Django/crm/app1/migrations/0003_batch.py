# Generated by Django 2.2.5 on 2019-09-24 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190924_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_Code', models.CharField(max_length=150)),
                ('Date', models.DateField()),
                ('Select_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course')),
            ],
        ),
    ]
