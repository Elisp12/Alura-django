from django.urls import path

from .views.login import login
from .views.cadastro import cadastro

urlpatterns = [
    path('login', login, name="login"),
    path('cadastro', cadastro, name='cadastro'),
]
