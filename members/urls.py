from django.urls import path
from . import views



urlpatterns = [
    path('main', views.main, name='main'),
    path('members/', views.members, name='members'),
    path ('members/details/<int:id>', views.details, name='details'),

    path ('testing/', views.testing, name='testing'),
    path ('testing/details/<int:id>', views.details, name='testing2'),


    # path('', views.homepage, ""),
    path('register', views.register, name= 'register'),
    path('mylogin', views.my_login, name= 'mylogin'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('user-logout', views.user_logout, name= 'user-logout'),
]