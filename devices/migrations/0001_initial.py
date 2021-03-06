# Generated by Django 2.2.2 on 2019-06-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('type', models.CharField(choices=[('JSON', 'json'), ('PLAINTEXT', 'plaintext'), ('BINARY', 'binary')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('properties', models.ManyToManyField(related_name='devices', to='devices.Property')),
            ],
        ),
    ]
