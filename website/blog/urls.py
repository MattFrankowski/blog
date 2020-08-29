from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogger/', views.bloggerPage, name='blogger'),
    path('blogger/create_post', views.createPost, name="create_post"),

    path('blogger/post/<str:post_id>', views.postPage, name='post'),
    path('blogger/post/<str:post_id>/update', views.updatePage, name='update_post'),
    path('blogger/post/<str:post_id>/delete', views.deletePage, name='delete_post'),

    path('about/', views.aboutPage, name='about'),

    path('register/', views.registerPage, name='register'),

    path('user/', views.userPage, name='user'),
    path('user/create_blog', views.createBlogPage, name='create_blog'),


]
