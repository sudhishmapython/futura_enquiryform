# Generated by Django 4.2.3 on 2023-07-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coding_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('completed_course', models.CharField(max_length=250)),
                ('year_of_passout', models.CharField(max_length=250)),
                ('college', models.CharField(max_length=250)),
                ('mobile_no', models.IntegerField()),
                ('technologies', models.CharField(max_length=250)),
                ('interested_field', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Noncoding_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
            ],
        ),
    ]
