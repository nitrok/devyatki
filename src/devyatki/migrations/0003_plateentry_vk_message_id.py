# Generated by Django 4.0.4 on 2022-05-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devyatki', '0002_plateentry_telegram_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plateentry',
            name='vk_message_id',
            field=models.IntegerField(default=0),
        ),
    ]
