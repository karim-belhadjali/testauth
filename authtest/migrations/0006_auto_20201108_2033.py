# Generated by Django 3.1.2 on 2020-11-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0005_auto_20201108_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
