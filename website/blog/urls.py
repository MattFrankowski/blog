from django.urls import path

from .views import *

urlpatterns = [
    path('', homePage, name='home'),
    path('blogger/', bloggerPage, name='blogger'),
    path('blogger/create_post', createPost, name="create_post"),
    path('blogger/create_post', createPost, name="create_post"),

    path('blogger/post/<str:post_id>', postPage, name='post'),
    path('blogger/post/<str:post_id>/update', updatePage, name='update_post'),
    path('blogger/post/<str:post_id>/delete', deletePage, name='delete_post'),

    path('blogger/<str:pk>', bloggerVisitPage, name='blogger_visit'),
    path('blogger/<str:pk>/post/<str:post_id>', postVisitPage, name='post_visit'),


    path('about/', aboutPage, name='about'),

    path('register/', registerPage, name='register'),

    path('user/', userPage, name='user'),
    path('user/create_blog', createBlogPage, name='create_blog'),


    path('search_results/', searchResultsPage, name='search_results'),
]
