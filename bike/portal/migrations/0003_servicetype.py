# Generated by Django 3.1.1 on 2020-09-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20200921_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('onhold', models.BooleanField(default=False)),
            ],
        ),
    ]
