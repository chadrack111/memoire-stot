from django.urls import path
from . import views

app_name = 'elearning'


urlpatterns = [
    path('', views.home, name='home'),
    path('elearning/courses/', views.course_list, name='course_list'),
    path('elearning/courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('elearning/login/', views.c_login, name='login'),
    path('elearning/register/', views.c_register, name='register'),
    
]
