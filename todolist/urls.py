from django.urls import path
from todolist.views import  show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import update_task
from todolist.views import delete_task
from todolist.views import get_todolist_json, add_todolist_item



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('add/', add_todolist_item, name = 'add_todolist_item'),
    path('json/', get_todolist_json, name = 'get_todolist_json'),

]