# Generated by Django 5.1.2 on 2024-11-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('descriprion', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
