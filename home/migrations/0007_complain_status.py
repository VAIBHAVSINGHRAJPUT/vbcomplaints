# Generated by Django 4.0.6 on 2022-07-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_account_delete_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]