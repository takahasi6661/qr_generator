# Generated by Django 3.1.3 on 2020-11-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('description', models.TextField(blank=True, db_index=True)),
                ('url', models.TextField(blank=True, db_index=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'sites',
            },
        ),
    ]
