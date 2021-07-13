from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todos',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
