"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist_app import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListMineTodoView.as_view(), name='list_todos'),
    path('create/', views.CreateTodoView.as_view(), name='create_todo'),
    path('update/<int:pk>', views.UpdateTodoView.as_view(), name='update_todo'),
    path('delete/<int:pk>', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('done/<int:pk>', views.todo_done, name='do_todo'),
    path('accounts/', include('django.contrib.auth.urls'), name='login_view'),

]
