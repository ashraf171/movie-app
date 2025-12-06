from rest_framework.routers import DefaultRouter
from .views import GenreViewSet,ActorViewSet,MovieViewSet,ReviewViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
router=DefaultRouter()
router.register(r'genres',GenreViewSet)
router.register(r'actors',ActorViewSet)
router.register(r'movies',MovieViewSet)
router.register(r'reviews',ReviewViewSet)



urlpatterns = [

    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    
]

urlpatterns+=router.urls