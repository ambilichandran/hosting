# Generated by Django 5.1.1 on 2024-09-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0008_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, max_length=50)),
                ('image', models.CharField(max_length=500)),
                ('qualification', models.CharField(blank=None, max_length=150)),
            ],
        ),
    ]
