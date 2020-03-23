# Generated by Django 3.0.3 on 2020-03-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('formulaID', models.IntegerField()),
                ('inversion', models.IntegerField()),
            ],
        ),
    ]
