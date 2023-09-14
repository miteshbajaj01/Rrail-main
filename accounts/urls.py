from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('book-ticket/', views.book_ticket, name='book-ticket'),
    path('bookings/', views.bookings, name='bookings'),
    path('oauth/', include('social_django.urls', namespace='social')),
]