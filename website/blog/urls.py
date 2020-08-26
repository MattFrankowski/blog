from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogger/<str:pk>', views.bloggerPage, name='blogger'),
    path('blogger/<str:pk>/create_post', views.createPost, name="create_post"),

    path('blogger/<str:pk>/post/<str:post_id>', views.postPage, name='post'),
    path('blogger/<str:pk>/post/<str:post_id>/update', views.updatePage, name='update_post'),
    path('blogger/<str:pk>/post/<str:post_id>/delete', views.deletePage, name='delete_post'),

    path('about/', views.aboutPage, name='about'),

    path('register/', views.registerPage, name='register'),

    path('user/<str:pk>', views.userPage, name='user'),
    path('user/<str:pk>/create_blog', views.createBlogPage, name='create_blog'),


]
