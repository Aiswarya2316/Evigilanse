# Generated by Django 5.1.1 on 2024-11-18 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='police',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='idproof',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
