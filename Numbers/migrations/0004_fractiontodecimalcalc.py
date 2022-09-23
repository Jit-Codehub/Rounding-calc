# Generated by Django 4.0.5 on 2022-09-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Numbers', '0003_quotientofnumberscalc'),
    ]

    operations = [
        migrations.CreateModel(
            name='fractionToDecimalCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.DecimalField(decimal_places=5, max_digits=5)),
                ('numa', models.PositiveIntegerField()),
                ('numb', models.PositiveIntegerField()),
            ],
        ),
    ]
