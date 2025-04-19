from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.userLogin, name='userLogin'),

    path('logout/', views.userLogout, name='userLogout'),

    path('register/', views.userRegister, name='userRegister'),
]