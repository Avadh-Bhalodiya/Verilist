from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('user/register/', UserRegisterCreateView.as_view(), name="user_create"),
    path('user/<slug:username>/', UserRegisterListView.as_view(), name="user_list_show"),    

    path('<slug:username>/checklists/<int:pk>/', ToDoModelSelectedList.as_view(),name="show_selected_todolist"),
    path('<slug:username>/checklists/', ToDoModelAllList.as_view(), name="show_todolist"),
    path('<slug:username>/checklist/new/', ToDoModelNewCreateList.as_view(), name="create_todolist"),
    path('<slug:username>/checklist/<int:pk>/', ToDoModelModifiedUpdateList.as_view(), name="update_todolist"),
    
    path('<slug:username>/checklists/<int:pk>/tasks', TaskViewList.as_view(),name="show_tasks"),
    path('<slug:username>/checklists/<int:pk>/new', TaskCreateList.as_view(),name="create_task"),
    path('<slug:username>/checklists/<int:id>/<int:pk>/', TaskUpdateList.as_view(),name="update_task"),
]
