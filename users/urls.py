from django.urls import path
from .views import signIn,signUp, signOut

urlpatterns = [
    path('login/', signIn, name='login'),
    path('logout/', signOut, name='logout'),
     path('register/', signUp, name='register')
]