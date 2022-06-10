# Generated by Django 4.0.5 on 2022-06-06 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_dead', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Escribe el nombre del género', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Escribe el título de la película', max_length=64)),
                ('summary', models.TextField(help_text='Resumen de la película', max_length=100)),
                ('estreno', models.CharField(help_text='Año de estreno', max_length=4)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director')),
                ('genre', models.ManyToManyField(to='catalog.genre')),
            ],
        ),
    ]