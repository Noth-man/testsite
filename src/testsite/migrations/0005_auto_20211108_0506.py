# Generated by Django 3.0.4 on 2021-11-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0004_auto_20211106_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]