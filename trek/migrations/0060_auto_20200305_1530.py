# Generated by Django 2.2.9 on 2020-03-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0059_aboutusdetail_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='speciality',
            field=models.CharField(blank=True, choices=[('Himalaya', 'Himalaya Tour'), ('Best', 'Best Offer'), ('Special', 'Special Package'), ('Pilgrim', 'Pilgirm Tour'), ('Yoga', 'Yoga Tour')], max_length=50, null=True),
        ),
    ]
