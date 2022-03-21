# Generated by Django 4.0.3 on 2022-03-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_email_frommail_email_tomail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='submittedOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]