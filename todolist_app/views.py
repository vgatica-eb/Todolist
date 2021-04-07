# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import ToDo
from .models import Priority
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse


class TodoListView(LoginRequiredMixin, ListView):
    model = ToDo


class CreateTodoView(LoginRequiredMixin, CreateView):
    model = ToDo
    fields = [
        'description',
        'priority',
    ]

    def get_success_url(self):
        return reverse('list_todos')

    def form_valid(self, form):
        form.instance.user_assigned = self.request.user
        return super(CreateTodoView, self).form_valid(form)


class CreatePriorityView(LoginRequiredMixin, CreateView):
    model = Priority
    fields = '__all__'
    reverse_lazy('create_priority')
    success_url = reverse_lazy('list_todos')


class UpdateTodoView(LoginRequiredMixin, UpdateView):
    model = ToDo
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('list_todos')


class DeleteTodoView(LoginRequiredMixin, DeleteView):
    model = ToDo

    def get_success_url(self):
        return reverse('list_todos')


@login_required
def todo_done(request, pk):
    # self.done = True
    # return reverse('list_todos')
    done_todo = ToDo.objects.get(pk=pk)
    done_todo.done = True
    done_todo.save()
    return redirect('list_todos')
