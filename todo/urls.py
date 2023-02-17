from django.urls import path
from .views import TaskList, TaskDetail, TaskComplete, TaskIncomplete

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('tasks/<int:pk>/complete/', TaskComplete.as_view()),
    path('tasks/<int:pk>/incomplete/', TaskIncomplete.as_view()),
]