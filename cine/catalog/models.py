from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=32, help_text='Escribe el nombre del género')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=64, help_text='Escribe el título de la película')
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=240, help_text='Resumen de la película')
    estreno = models.CharField(max_length=4, help_text='Año de estreno')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_dead = models.DateField('Died', null=True, blank=True)


    def __str__(self):
        return '%s  %s' % (self.first_name, self.last_name)
