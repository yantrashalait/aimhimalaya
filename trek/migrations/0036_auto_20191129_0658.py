# Generated by Django 2.2.5 on 2019-11-29 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0035_auto_20191129_0617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packageitinerary',
            options={'ordering': ['day']},
        ),
    ]
