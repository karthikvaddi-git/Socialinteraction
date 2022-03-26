# Generated by Django 4.0.3 on 2022-03-26 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialapp', '0003_alter_message_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=20, unique=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('groupmembers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupmember', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='socialapp.tag')),
            ],
        ),
    ]
