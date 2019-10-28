from django.urls import path

from . import views

app_name = 'slend'
urlpatterns = [
    path('', views.snake_def , name = 'snake_def'),
]