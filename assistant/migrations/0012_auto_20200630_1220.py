# Generated by Django 2.2.10 on 2020-06-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0011_auto_20200630_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinfo',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
