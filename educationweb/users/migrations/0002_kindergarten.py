# Generated by Django 3.2 on 2021-04-10 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('seatLimit', models.IntegerField()),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('myTeacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
    ]
