# Generated by Django 2.2.5 on 2019-12-03 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0039_auto_20191201_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerimage',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='trek.Package'),
        ),
    ]
