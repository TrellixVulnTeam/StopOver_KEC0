from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='map-home'),
    path('', views.get_mylocation),
]
