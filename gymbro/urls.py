from django.urls import path
from . import views

urlpatterns = [
    # This is the path and method to view the login and registration screen.
    path('', views.Reg_and_Login_index),
    path('home', views.dashboard),
    path('workout/<int:workout_id>', views.show_workout),
    path('exercise/<int:exercise_id>', views.show_exercise),
    path('exercise/<int:workout_id>/<int:exercise_id>', views.show_exercise),
    # Not sure what the ↑ line or ↓ line do. They both point to views.show_exercise
    path('meet_the_team', views.show_the_team),
    path('myprofile', views.show_myprofile),
    path('myprofile/<int:link_id>', views.show_data_visualization),
    path('edit_profile', views.edit_profile),
    path('create_user', views.create_user),
    path('login', views.login),
    path('begin_workout', views.begin_workout),
    path('add_sets_data/<int:workout_id>/<int:exercise_id>', views.add_sets_data),
    path('logout',views.logout),
]