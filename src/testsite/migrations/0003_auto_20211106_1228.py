# Generated by Django 3.0.4 on 2021-11-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0002_auto_20211105_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='paremt_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='threads',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]