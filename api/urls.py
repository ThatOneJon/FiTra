from django.urls import path
from . import views




urlpatterns = [
    path('', views.api_Overview, name ="info"),
    path('profile/<str:pk>', views.get_Profile_Data, name ="profile"),
    path('workout/<str:pk>', views.get_Workout_Data, name ="workoutData")
]