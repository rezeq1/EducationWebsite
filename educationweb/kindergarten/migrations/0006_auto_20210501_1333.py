# Generated by Django 3.1.7 on 2021-05-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten', '0005_story_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qustion',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quiz',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='storypage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Qustion',
        ),
    ]