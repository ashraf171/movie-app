from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GenreSerializer,ActorSerializer,MovieSerializer,ReviewSerializer,RigesterSerializer
from .models import Genre,Actor,Movie,Review
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .permission import IsAdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class PaginatorView(PageNumberPagination):
    page_size=5
    page_size_query_param ='page_size'
    max_page_size=25

class GenreViewSet(viewsets.ModelViewSet):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    permission_classes=[IsAdminOrReadOnly]
    pagination_class=PaginatorView



class ActorViewSet(viewsets.ModelViewSet):
    queryset=Actor.objects.all()
    serializer_class=ActorSerializer
    permission_classes=[IsAdminOrReadOnly]
    pagination_class=PaginatorView



class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]

    filterset_fields = ['genres', 'actors', 'release_year', 'rating']
    search_fields = ['title', 'description', 'actors__name', 'genres__name']  
    ordering_fields = ['release_year', 'rating', 'title']
    pagination_class=PaginatorView


class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    pagination_class=PaginatorView

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class RigesterViewSet(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RigesterSerializer