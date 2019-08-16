# Generated by Django 2.2.2 on 2019-06-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0006_auto_20190610_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('happy_review', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='clients/profile/')),
                ('cover_picture', models.ImageField(upload_to='clients/cover/')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='header/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
    ]
