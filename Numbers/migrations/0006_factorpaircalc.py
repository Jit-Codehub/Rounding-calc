# Generated by Django 4.0.5 on 2022-09-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Numbers', '0005_alter_fractiontodecimalcalc_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='factorPairCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField()),
                ('facs', models.CharField(max_length=255)),
            ],
        ),
    ]
