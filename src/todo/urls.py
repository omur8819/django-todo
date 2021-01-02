from django.urls import path
from .views import home, todo_list, todo_create, todo_update

urlpatterns = [
    path("", home, name="house"),
    path("list/", todo_list, name="todo-list"),
    path("create/", todo_create, name="todo_create"),
    path("<int:id>/update", todo_update, name="todo-update"),
    
]
