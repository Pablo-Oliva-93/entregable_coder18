# Generated by Django 4.1.4 on 2022-12-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('altura', models.FloatField()),
                ('casado', models.BooleanField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
