# Generated by Django 2.2.2 on 2019-06-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('private', models.CharField(blank=True, max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
