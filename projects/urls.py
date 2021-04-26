from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path('', views.land_page, name='landing'),
    path('detail/<int:project_id>', views.detail, name='detail'),
]