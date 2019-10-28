from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index , name = 'index'),
    path('<int:stat_id>/', views.detail , name = 'detail'),
    path('<int:stat_id>/leave_coment/', views.leave_coment , name = 'leave_coment')
]