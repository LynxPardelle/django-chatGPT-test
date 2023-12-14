from django.urls import path, include
from . import views

urlpatterns = [
    path('author', views.author),
    path('contact/', include('contact.urls')),
    path('user/', include('user.urls')),
    path('specific/', include('specific.urls')),
]
