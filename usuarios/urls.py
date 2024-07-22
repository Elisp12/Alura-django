from django.urls import path

from .views.login import login

urlpatterns = [
    path('login', login, name="login"),
]
