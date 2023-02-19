from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('room/<str:pk>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),

    path('delete/<str:pk>/', views.delete, name='delete'),
    path(
        'delete_message/<str:pk>/',
        views.delete_message,
        name="delete_message"),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),

    path('profile/<str:pk>/', views.user_profile, name="user_profile"),
    path('update_user', views.update_user, name="update_user"),
]
