# Generated by Django 3.1.4 on 2021-01-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210114_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
