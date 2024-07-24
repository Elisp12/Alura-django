from django.urls import path

from apps.usuarios.views.login import login
from apps.usuarios.views.cadastro import cadastro
from apps.usuarios.views.logout import logout
from apps.usuarios.views.home_usuario import home_usuario


urlpatterns = [
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name = 'logout'),
    path('home/usuario/', home_usuario, name = 'home_usuario'),
]
