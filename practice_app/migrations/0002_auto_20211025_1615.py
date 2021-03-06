# Generated by Django 3.2.8 on 2021-10-25 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(max_length=1000, upload_to='avatars/'),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('LT', 'light tank'), ('MT', 'medium tank'), ('HT', 'heavy tank'), ('TD', 'tank destroyer'), ('SPG', 'SPG')], default='MT', max_length=10)),
                ('capacity', models.IntegerField(default=-1)),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice_app.manufacturer')),
            ],
        ),
    ]
