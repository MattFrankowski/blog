from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogger/<str:pk>', views.bloggerPage, name='blogger'),
    path('blogger/<str:pk>/create_post', views.createPost, name="create_post"),

    path('blogger/<str:pk>/post/<str:post_id>', views.postPage, name='post'),
    path('blogger/<str:pk>/post/<str:post_id>/update', views.updatePage, name='update_post'),
    path('blogger/<str:pk>/post/<str:post_id>/delete', views.deletePage, name='delete_post'),

    path('register/', views.registerPage, name='register'),

    # path('register/', views.registerPage, name='register'),
    # path('login/', views.loginPage, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    #
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_sent'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
