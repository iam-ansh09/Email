# Generated by Django 4.0.3 on 2022-03-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='fromMail',
            field=models.EmailField(default='xyz@giet.edu', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='toMail',
            field=models.EmailField(default='xyz@giet.edu', max_length=254),
            preserve_default=False,
        ),
    ]
