# Generated by Django 3.1.1 on 2020-09-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20200926_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.TextField(default='Scheduled', max_length=30),
        ),
    ]
