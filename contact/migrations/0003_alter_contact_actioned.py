# Generated by Django 3.2 on 2022-08-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_actioned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='actioned',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed')], max_length=50),
        ),
    ]