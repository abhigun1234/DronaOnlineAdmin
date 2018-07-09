# Generated by Django 2.0.6 on 2018-07-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('fees', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('imageUrl', models.CharField(max_length=30)),
                ('videoUrl', models.CharField(max_length=30)),
            ],
        ),
    ]
