# Generated by Django 3.1.2 on 2020-11-08 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0004_merge_20201108_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authtest.role'),
            preserve_default=False,
        ),
    ]
