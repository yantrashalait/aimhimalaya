# Generated by Django 2.2.5 on 2019-09-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0027_auto_20190923_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trippersonalinfo',
            name='trip_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='trek.TripBooking'),
        ),
    ]
