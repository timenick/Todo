from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from todolist import models


def todo_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            models.Todo.objects.create(title=title)
    list = models.Todo.objects.all()
    return render(request, 'todolist.html', locals())


def complete(request, idx):
    todo_item = get_object_or_404(models.Todo, id=idx)
    todo_item.completed = True
    todo_item.save()
    return HttpResponsePermanentRedirect('/')


def delete(request, idx):
    todo = get_object_or_404(models.Todo, id=idx)
    todo.delete()
    return HttpResponsePermanentRedirect('/')