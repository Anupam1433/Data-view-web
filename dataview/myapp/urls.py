from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.show_data, name='show_data'),
]
