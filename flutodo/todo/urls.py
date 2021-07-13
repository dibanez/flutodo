
from django.urls import path
from todo.views import TodoListView, TodoCreateView, TodoMarkDone

from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('create_task/', TodoCreateView.as_view(), name='create_task'),
    path('update_task/', TodoMarkDone.as_view(), name='update_task'),
]
