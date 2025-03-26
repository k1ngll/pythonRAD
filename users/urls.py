from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name='login'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('sair', views.signout, name='sair'),

    #Recuperar Senha
    path('recuperar_senha_form/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset_form'),
    path('recuperar_senha_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('recuperar_senha_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('recuperar_senha_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]