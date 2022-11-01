from django.urls import path
from . import views




urlpatterns = [
    path('', views.api_Overview, name ="info"),
    path('profile/<str:pk>', views.get_Profile_Data, name ="profile"),
    path('workout/<str:pk>', views.get_Workout_Data, name ="workoutData"),
    path('createUser/', views.generate_new_user, name ="createUser"),
    path('createWorkout/', views.generate_new_workout, name="createWorkout"),
    path('createExercise/<str:pk>', views.generate_new_exercise, name="createExercise"),
    path('editProfile/<str:pk>', views.edit_existing_profile, name='editProfile'),
    path('editExercise/weight/<str:pk>', views.edit_existing_weight_exercise, name ='editWeight'),
    path('editExercise/cardio/<str:pk>', views.edit_existing_cardio_exercise, name ='editCardio'),

]