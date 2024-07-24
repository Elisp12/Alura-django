from django.urls import path

from apps.usuarios.views.login import login
from apps.usuarios.views.cadastro import cadastro
from apps.usuarios.views.logout import logout

urlpatterns = [
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name = 'logout'),
]
