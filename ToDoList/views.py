from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse("仮のトップページ")
    return render(request, "ToDoList/index.html")

# Create your views here.
