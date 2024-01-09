from django.shortcuts import render


# Create your views here.
def index(request):
    tasks = ["Task 1", "Task 2", "Task 3"]

    return render(request, "tasks/index.html", {"tasks": tasks})
