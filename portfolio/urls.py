from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('/projects', views.projects,name="projects"),
    path('/cv', views.cv,name="cv"),
    path('/hire-me', views.hire_me,name="hire-me"),
]
