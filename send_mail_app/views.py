from django.http import HttpResponse
from django.shortcuts import render
from send_mail_app.tasks import send_mail_func

def send_mail_to_all(request):
  send_mail_func()
  return HttpResponse("Sent")