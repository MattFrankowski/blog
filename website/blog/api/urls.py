from django.urls import path
from .views import postDetailView

urlpatterns = [
    path('post/<str:pk>/', postDetailView, name='post-detail'),
]