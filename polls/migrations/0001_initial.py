# Generated by Django 3.2.6 on 2022-05-06 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('cover', models.ImageField(upload_to='cover/')),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='updated')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='description')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='File')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='updated by')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ('-created',),
                'get_latest_by': '-created',
                'abstract': False,
            },
        ),
    ]
