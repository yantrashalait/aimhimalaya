# Generated by Django 2.2.5 on 2019-12-09 13:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0051_auto_20191209_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]