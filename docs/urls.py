from django.urls import path
from . import views

urlpatterns = [
    path('author', views.author, name='author'),
    path('createDoc', views.createDoc, name='createDoc'),
    path('createDocSection/<int:doc_id>',
         views.createDocSection, name='createDocSection'),
    path('readMany', views.readMany, name='readMany'),
    path('read/<int:doc_id>', views.read, name='read'),
    path('updateDoc/<int:doc_id>', views.updateDoc, name='updateDoc'),
    path('updateDocSection/<int:doc_section_id>',
         views.updateDocSection, name='updateDocSection'),
    path('deleteDoc/<int:doc_id>', views.deleteDoc, name='deleteDoc'),
    path('deleteDocSection/<int:doc_section_id>',
         views.deleteDocSection, name='deleteDocSection'),
]
