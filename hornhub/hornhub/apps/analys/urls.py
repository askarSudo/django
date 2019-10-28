from django.urls import path

from . import views

app_name = 'analys'
urlpatterns = [
    path('', views.analys_def , name = 'analys_def'),
]