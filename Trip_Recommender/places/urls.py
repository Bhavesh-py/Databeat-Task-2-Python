from django.contrib import admin
from django.urls import path
from .views import PlaceViewSet, UserAPUView

urlpatterns = [
    path('places', PlaceViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('places/<str:pk>', PlaceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'remove'
    })),
        path('user', UserAPUView.as_view())
]