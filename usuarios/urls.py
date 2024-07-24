from django.urls import path

from .views.login import login
from .views.cadastro import cadastro
from .views.logout import logout

urlpatterns = [
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name = 'logout'),
]
