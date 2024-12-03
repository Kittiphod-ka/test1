from django.urls import path
from .views import *

urlpatterns = [
    path('course_search/', course_search, name='course_search'),
    path('update/<str:pk>/', CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
    path('courses/', course_list.as_view(), name='course_list'),

    ]
