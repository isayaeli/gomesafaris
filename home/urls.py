from django.urls import path
from .views import home, details

urlpatterns = [
    path('', home, name='home' ),
    path('details/<int:id>/', details, name="details")
]