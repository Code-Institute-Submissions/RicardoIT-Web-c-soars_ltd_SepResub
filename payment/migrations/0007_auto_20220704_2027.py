# Generated by Django 3.2 on 2022-07-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_order_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_briefcase',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
