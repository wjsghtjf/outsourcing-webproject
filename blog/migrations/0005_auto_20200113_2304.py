# Generated by Django 2.2.1 on 2020-01-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200111_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumname_image',
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
