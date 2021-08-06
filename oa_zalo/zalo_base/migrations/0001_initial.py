# Generated by Django 3.2.4 on 2021-07-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZaloMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('regist_phone', models.CharField(max_length=200)),
                ('regist_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ZaloUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]