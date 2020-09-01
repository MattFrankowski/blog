from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogger/', views.bloggerPage, name='blogger'),
    path('blogger/create_post', views.createPost, name="create_post"),

    path('blogger/post/<str:post_id>', views.postPage, name='post'),
    path('blogger/post/<str:post_id>/update', views.updatePage, name='update_post'),
    path('blogger/post/<str:post_id>/delete', views.deletePage, name='delete_post'),

    path('blogger/<str:pk>', views.bloggerVisitPage, name='blogger_visit'),
    path('blogger/<str:pk>/post/<str:post_id>', views.postVisitPage, name='post_visit'),


    path('about/', views.aboutPage, name='about'),

    path('register/', views.registerPage, name='register'),

    path('user/', views.userPage, name='user'),
    path('user/create_blog', views.createBlogPage, name='create_blog'),

    path('search_results/', views.searchResultsPage, name='search_results'),
]
