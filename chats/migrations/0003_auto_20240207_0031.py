# Generated by Django 3.2.12 on 2024-02-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]