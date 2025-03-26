from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate,logout 
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'users/index.html')

def cadastrar(request):
    if request.method == "POST":
        username = request.POST.get('nome') 
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')

        if not username or not email or not senha or not confirma_senha:
            messages.error(request, "Todos os campos são obrigatórios!")
            return redirect('cadastrar')

        if senha != confirma_senha:
            messages.error(request, "As senhas não coincidem!")
            return redirect('cadastrar')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "E-mail inválido!")
            return redirect('cadastrar')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Esse e-mail já está registrado!")
            return redirect('cadastrar')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está em uso!")
            return redirect('cadastrar')

        usuario = User.objects.create_user(username=username, email=email, password=senha)
        usuario.first_name = username
        usuario.save()

        messages.success(request, "Sua conta foi criada com sucesso!")
        return redirect('login')  

    return render(request, 'users/cadastrar.html')

def login(request):

    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=email, password=senha)
        print(user)

        if user is not None:
            print("aqui")
            auth_login(request, user)
            nome = user.first_name
            return render(request, 'users/index.html', {'nome': nome})

        else:
            messages.error(request, "Email ou senha errados.")
            return redirect('home')

    return render(request, 'users/login.html')

def signout(request):
    logout(request)
    return redirect('home')




