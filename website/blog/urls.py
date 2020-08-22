from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogger/<str:pk>', views.bloggerPage, name='blogger'),
    path('blogger/<str:pk>/create_post', views.createPost, name="create_post"),

    path('blogger/<str:pk>/post/<str:post_id>', views.postPage, name='post'),
    path('blogger/<str:pk>/post/<str:post_id>/update', views.updatePage, name='update_post'),
    path('blogger/<str:pk>/post/<str:post_id>/delete', views.deletePage, name='delete_post'),
]
