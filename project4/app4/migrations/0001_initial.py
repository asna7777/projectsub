# Generated by Django 5.0.3 on 2024-05-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=50)),
                ('myaddress', models.CharField(max_length=50)),
            ],
        ),
    ]
