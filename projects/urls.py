from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.land_page, name='land_page'),
    path('<int:project_pk>', views.detail, name='detail'),
]