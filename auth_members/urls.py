from django.urls import path

from . import views
urlpatterns = [
    path('create/', views.create_member, name='create_member'),
]