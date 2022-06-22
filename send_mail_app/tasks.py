from Verilist import settings
from celery import shared_task
from django.core.mail import send_mail
from Verilist import settings
from django.contrib.auth.models import User
from api.models import *

@shared_task(bind=True)
def send_mail_func(self):
  users = User.objects.all()
  print(users)
  for user in users:
    todo_list_objs = ToDoList.objects.filter(creator=user).values_list('id', flat=True)
    pending_task_objs = Task.objects.filter(parent_list_name__id__in=list(todo_list_objs), status='pending').values_list('task_name', flat=True)
    completed_task_objs = Task.objects.filter(parent_list_name__id__in=list(todo_list_objs), status='completed').values_list('task_name', flat=True)
    mail_subject = "Hie This is your today Task"
    message = f'Pending Tasks : {list(pending_task_objs)} \n Completed Tasks : {list(completed_task_objs)}'
    to_email = user.email
    send_mail(
      subject = mail_subject,
      message = message,
      from_email = settings.EMAIL_HOST_USER,
      recipient_list = [to_email],
      fail_silently = True,
    )
  return "Done"
