# Generated by Django 2.1 on 2019-02-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=500)),
            ],
        ),
    ]
