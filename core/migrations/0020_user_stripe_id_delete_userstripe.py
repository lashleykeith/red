# Generated by Django 5.0 on 2024-03-25 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_productorder_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='UserStripe',
        ),
    ]
