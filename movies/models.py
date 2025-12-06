from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):
    name=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name
    

class Actor(models.Model):
    name=models.CharField(max_length=120,db_index=True)
    birth_year=models.IntegerField(
        validators=[MinValueValidator(1990),MaxValueValidator(2025)]
    )
    country=models.CharField(max_length=120)


    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title=models.CharField(max_length=120,db_index=True)
    description=models.TextField()
    release_year=models.IntegerField(default=0)
    rating=models.SmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )
    genres=models.ManyToManyField(Genre)
    actors=models.ManyToManyField(Actor)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
    rating=models.SmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.rating}'
    