# Generated by Django 2.1 on 2019-07-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=64),
        ),
    ]