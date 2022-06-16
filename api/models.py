from django.db import models
from django.contrib.auth.models import User

class ToDoApp(models.Model):
  name = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)
  pwd = models.CharField(max_length=30)
  date_created = models.DateTimeField(auto_now_add=True)
  taskname = models.CharField(max_length=100)
  parentlistname = models.CharField(max_length=50)


class ToDoList(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=100)
  creation_date = models.DateField()
  due_date = models.DateField()

  def __str__(self) -> str:
    return self.creator.username


class Task(models.Model):
  parent_list_name = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
  task_name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  data_creation = models.DateField()
  priority_choice = [
    ('high', 'High'),
    ('low', 'Low'),
    ('medium', 'Medium'),
  ]
  priority = models.CharField(max_length=10, choices=priority_choice)
  status_choice = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('inactive', 'In-active'),
  ]
  status = models.CharField(max_length=10, choices=status_choice)

  def __str__(self) -> str:
    return self.task_name