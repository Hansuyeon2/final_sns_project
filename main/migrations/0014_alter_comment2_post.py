# Generated by Django 4.0.5 on 2022-06-30 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_comment2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment2',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment2s', to='main.post'),
        ),
    ]
