# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('profile', views.profile, name='profile'),
#     path('signup', views.signup, name='signup'),
# ]

from django.urls import path
from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name ="index"),
    path('home/', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('add/', views.add_file, name='add_file'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

