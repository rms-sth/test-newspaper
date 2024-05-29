# Generated by Django 5.0.4 on 2024-05-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]