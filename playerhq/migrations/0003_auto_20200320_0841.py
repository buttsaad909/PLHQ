# Generated by Django 2.2.3 on 2020-03-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerhq', '0002_auto_20200320_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='GameImage',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='GameImage',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
