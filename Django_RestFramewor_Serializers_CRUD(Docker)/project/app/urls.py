from django.contrib import admin
from django.urls import path, include
from app import views
from app.views import Index

urlpatterns = [
    
    
    path("task-list/",views.taskList),
     path("task-detail/<str:pk>/",views.taskDetail),
     path("task-create/",views.taskCreate),
      path("task-update/<str:pk>/",views.taskUpdate),
      path("task-delete/<str:pk>/",views.taskUpdate),
]