from django.shortcuts import render

# Create your views here.

def index(request):
    msg = "Hello World!"
    return render(request, "hello/index.html",{
        "message":msg
    })