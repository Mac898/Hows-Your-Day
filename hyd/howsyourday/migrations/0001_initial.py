# Generated by Django 3.2.5 on 2022-02-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userText', models.CharField(max_length=100)),
                ('publishDate', models.DateTimeField(verbose_name='date published')),
                ('userColor', models.CharField(max_length=6)),
                ('userName', models.CharField(max_length=25)),
            ],
        ),
    ]