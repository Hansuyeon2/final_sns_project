# Generated by Django 4.0.4 on 2022-07-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_blog_test_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.AddField(
            model_name='blog',
            name='genre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]