# Generated by Django 5.0.1 on 2024-11-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='Email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
