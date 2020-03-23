from django.shortcuts import render
from django.utils import timezone
from . import models


def homepage(request):

    return render(request, 'todolist_app/index.html')


def add_do(request):
    content_added = request.POST.get('content')
    date_add = timezone.now()

    models.Todo.objects.create(text=content_added, added_date=date_add)

    todo_items = models.Todo.objects.all().order_by('-added_date')

    todo_items_list = {
        'todo_items': todo_items,
    }

    return render(request, 'todolist_app/index.html', todo_items_list)
