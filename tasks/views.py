from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Index view
    A view for tasks index page. Lists all user's tasks.

    """
    if "tasks" not in request.session:
        request.session["tasks"] = []

    tasks = request.session["tasks"]
    return render(request, "tasks/index.html", {"tasks": tasks})


def add(request: HttpRequest) -> HttpResponse:
    """Add view
    A view for adding a new task. Only accepts POST requests with a `task`
    parameter in the body and adds it to the user's tasks.

    """
    if request.method == "POST":
        task = request.POST.get("task")
        request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))

    return render(request, "tasks/add.html")
