# Generated by Django 2.1.7 on 2019-05-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20190330_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='colour',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='seat_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
