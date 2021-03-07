# Generated by Django 3.1.7 on 2021-03-07 08:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitebp', '0005_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sitebp.exercise'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 7, 8, 18, 39, 786346)),
        ),
        migrations.AlterField(
            model_name='answers',
            name='vote',
            field=models.IntegerField(default=100),
        ),
    ]
