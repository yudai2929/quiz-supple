# Generated by Django 4.0.1 on 2022-04-12 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('filed', models.CharField(max_length=50)),
                ('choice1', models.CharField(max_length=255)),
                ('choice2', models.CharField(max_length=255)),
                ('choice3', models.CharField(max_length=255)),
                ('choice4', models.CharField(max_length=255)),
                ('answer', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('comprehension', models.CharField(max_length=10)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 4, 12, 13, 7, 39, 955755, tzinfo=utc))),
            ],
        ),
    ]
