from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


from rest_framework import viewsets
from rest_framework import permissions

from todo.models import Todo
from todo.serializers import TodoSerializer

import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todo_list"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        todo_text = request.POST.get('todo_text')
        response_data = {}

        todo = Todo(name=todo_text, user=request.user)
        todo.save()

        response_data['result'] = 'Create todo successful!'
        response_data['name'] = todo.name
        response_data['user'] = todo.user.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

class TodoMarkDone(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        todo_item = request.POST.get('item')
        response_data = {}

        todo = get_object_or_404(Todo, pk=todo_item)

        if todo.isComplete == True :
            todo.isComplete = False
        else:
            todo.isComplete = True
        todo.save()
        
        return HttpResponse(
            json.dumps('    '),
            content_type="application/json"
        )   
 