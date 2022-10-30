from django.urls import path
from . import views




urlpatterns = [
    path('', views.api_Overview, name ="info"),
    path('profile/', views.get_Profile_Data, name ="profile")
]