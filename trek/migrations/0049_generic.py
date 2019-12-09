# Generated by Django 2.2.5 on 2019-12-09 04:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0048_auto_20191208_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(help_text='Image size: width=746px height=300px', upload_to='generics/')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
