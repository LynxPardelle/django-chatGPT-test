from django.urls import path
from . import user_actions

urlpatterns = [
    path('author', user_actions.author),
]
