# Generated by Django 4.0.4 on 2022-04-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobreviventes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='verifcaitens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inseridos', models.BooleanField()),
            ],
        ),
    ]