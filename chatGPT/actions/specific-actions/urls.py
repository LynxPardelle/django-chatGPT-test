from django.urls import path
from . import specific_actions

urlpatterns = [
    path('author', specific_actions.author),
]
