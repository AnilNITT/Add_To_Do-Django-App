from todos.views import TodosAPIView, TodoDetailAPIView , CreateTodoAPIView, TodoListAPIView
from django.urls import path

urlpatterns = [
    # Combine path for get n post (create n get)
    path("", TodosAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailAPIView.as_view(), name="todo"),

    # path('create',CreateTodoAPIView.as_view() ,name='create-todo'),
    # path('list',TodoListAPIView.as_view() ,name='list-todo'),
]