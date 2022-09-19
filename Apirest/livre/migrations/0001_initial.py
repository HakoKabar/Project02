# Generated by Django 4.1.1 on 2022-09-19 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LivreListe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date_de_sorti', models.DateField()),
                ('favorite', models.BooleanField()),
                ('Liste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livre.livreliste')),
            ],
        ),
    ]