# Generated by Django 5.1.1 on 2024-10-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
                ('data', models.DateField()),
                ('instruction', models.CharField(max_length=200)),
            ],
        ),
    ]