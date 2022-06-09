from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('users', views.users, name='users'),
    path('profile/<id>/', views.profile, name='profile'),
    re_path(r'urlparams/$', views.urlparams, name='urlparams'),
]
