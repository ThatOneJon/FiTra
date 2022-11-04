from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.api_Overview, name ="info"),
    path('profile/<str:pk>', views.get_Profile_Data, name ="profile"),
    path('workout/<str:pk>', views.get_Workout_Data, name ="workoutData"),
    path('allWorkouts/', views.get_all_Workouts, name ="allWorkouts"),

    path('createUser/', views.generate_new_user, name ="createUser"),
    path('createWorkout/', views.generate_new_workout, name="createWorkout"),
    path('createExercise/<str:pk>', views.generate_new_exercise, name="createExercise"),
    path('editProfile/<str:pk>', views.edit_existing_profile, name='editProfile'),
    path('editExercise/weight/<str:pk>', views.edit_existing_weight_exercise, name ='editWeight'),
    path('editExercise/cardio/<str:pk>', views.edit_existing_cardio_exercise, name ='editCardio'),
    path('deleteProfile/<str:pk>', views.delete_profile, name ="deleteProfile"),
    path('deleteExercise/<str:pk>', views.delete_exercise, name ="deleteExercise"),
    path('deleteWorkout/<str:pk>', views.delete_workout, name="deleteWorkout"),

    path('api-auth/', include('rest_framework.urls')),
    #This adds login to the browseable url of the API

]