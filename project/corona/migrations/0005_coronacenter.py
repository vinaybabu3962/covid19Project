# Generated by Django 2.2 on 2020-09-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0004_coronarapid'),
    ]

    operations = [
        migrations.CreateModel(
            name='coronaCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=200)),
                ('centers', models.CharField(max_length=2000)),
            ],
        ),
    ]
