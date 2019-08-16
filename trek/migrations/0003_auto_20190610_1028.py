# Generated by Django 2.2.2 on 2019-06-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0002_package_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='package',
            name='speciality',
            field=models.CharField(blank=True, choices=[('Awesome Tour', 'Awesome'), ('Best Offer', 'Best'), ('Special Package', 'Special'), ('Popular Tour', 'Popular')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
