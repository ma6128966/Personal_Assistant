# Generated by Django 2.2.10 on 2020-07-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0018_auto_20200702_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_url',
            field=models.CharField(default='#', max_length=40),
        ),
    ]