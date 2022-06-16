from .models import User, ToDoList, Task
from .serializers import RegisterSerializer, ToDoListSerializer, TaskSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class UserRegisterCreateView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

class UserRegisterListView(ListAPIView):
  serializer_class = ToDoListSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return ToDoList.objects.filter(creator=user)

class ToDoModelSelectedList(RetrieveAPIView):
  queryset = ToDoList.objects.all()
  serializer_class = ToDoListSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return ToDoList.objects.filter(creator=user)

class ToDoModelAllList(ListAPIView):
  queryset = ToDoList.objects.all()
  serializer_class = ToDoListSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return ToDoList.objects.filter(creator=user)


class ToDoModelNewCreateList(CreateAPIView):
  queryset = ToDoList.objects.all()
  serializer_class = ToDoListSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

class ToDoModelModifiedUpdateList(UpdateAPIView):
  queryset = ToDoList.objects.all()
  serializer_class = ToDoListSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]


class TaskViewList(RetrieveAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

class TaskCreateList(CreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

class TaskUpdateList(UpdateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticated]

  # def get_queryset(self, *args, **kwargs):
  #   id = self.kwargs.get('id')
  #   todolist_obj = ToDoList.objects.get(id=id)
  #   return Task.objects.get(parent_list_name=todolist_obj)

