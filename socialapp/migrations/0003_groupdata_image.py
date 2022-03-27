# Generated by Django 4.0.3 on 2022-03-26 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_tag_groupdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupdata',
            name='image',
            field=models.ImageField(default=' ', upload_to='media/dynamic/img/user_image', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]