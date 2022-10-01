# Generated by Django 4.1.1 on 2022-10-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rollno', models.IntegerField()),
                ('marks', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]