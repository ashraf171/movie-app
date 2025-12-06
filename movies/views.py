from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GenreSerializer,ActorSerializer,MovieSerializer,ReviewSerializer
from .models import Genre,Actor,Movie,Review
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]



class ActorViewSet(viewsets.ModelViewSet):
    queryset=Actor.objects.all()
    serializer_class=ActorSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)