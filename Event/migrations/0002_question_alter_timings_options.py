# Generated by Django 4.0.3 on 2022-03-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='timings',
            options={'verbose_name_plural': 'Timings'},
        ),
    ]
