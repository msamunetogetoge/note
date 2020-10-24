from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def select_model(request):
    return render(request, "app/index.html" )


def select_data(request):
    return render(request, "app/select_data.html")
    
def calculation(request):
    return render(request, "app/calculation.html")
                

def get_result(request):
    return render(request, "app/get_result.html")

def help(request):
    return render(request, "app/help.html")
