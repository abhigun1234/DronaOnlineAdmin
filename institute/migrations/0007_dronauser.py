# Generated by Django 2.0.6 on 2018-10-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_auto_20181005_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='dronauser',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('birth_date', models.DateField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=30)),
            ],
        ),
    ]
