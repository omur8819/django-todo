from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "todo/home.html")

def todo_list
