from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_user),
    path('register', views.register_user),
    path('signOut', views.sign_out),
    path('', views.home),
]
