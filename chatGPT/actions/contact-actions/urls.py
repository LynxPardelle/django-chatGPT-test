from django.urls import path
from . import contact_actions

urlpatterns = [
    path('author', contact_actions.author),
]
