# Generated by Django 3.0.4 on 2021-11-05 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('paremt_id', models.IntegerField()),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('thread_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsite.Threads')),
            ],
        ),
    ]