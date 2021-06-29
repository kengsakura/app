# Generated by Django 3.2 on 2021-05-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20210517_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='level',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='minoractivity',
            name='money_ask',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
