# Generated by Django 5.1.3 on 2024-12-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('enroll_date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')])),
            ],
        ),
    ]