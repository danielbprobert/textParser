# Generated by Django 5.1.4 on 2024-12-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_num_characters_transaction_num_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='duration_ms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='duration_ms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
