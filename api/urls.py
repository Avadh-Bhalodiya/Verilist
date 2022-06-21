from django.urls import path
from api.views import *
from send_mail_app.views import *

urlpatterns = [
    path('sendmail/', send_mail_to_all, name="sendmail_to_all"),
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