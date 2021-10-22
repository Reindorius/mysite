# Generated by Django 3.2.8 on 2021-10-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='uploads/avatars/')),
                ('dob', models.DateField()),
            ],
        ),
    ]