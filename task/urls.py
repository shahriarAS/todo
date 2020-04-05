from django.urls import path
from .views import TaskList, update, delete

urlpatterns = [
    path('', TaskList, name="TaskList"),
    path('update/<int:pk>', update, name="update"),
    path('delete/<int:pk>', delete, name="delete"),
]
