from django.shortcuts import render
from .models import Todo


def index(request):
    todotask = Todo.objects.all()[:10]

    context = {
        'todotask': todotask
    }
    return render(request, 'index.html', context)

