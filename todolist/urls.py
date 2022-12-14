import imp
from django.urls import path

from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import show_todolist
from todolist.views import create_new_task
from todolist.views import update_status
from todolist.views import delete_task, show_json,add_task
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_new_task, name='create-new-task'),
    path('update-status/<int:pk>', update_status, name='update-status'),
    path('delete-task/<int:pk>', delete_task, name='delete-task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
]