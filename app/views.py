from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app.models import *

# Create your views here.

def index(request):
    return render(request, "app/index.html",{
        "models":MlModel.objects.all()
    })

def select_model(request):
    if request.method  =="POST":
        try:
            code           = request.POST["selected_model"]
            model          = MlModel.objects.get(code=code)
            selected_model = selectedModel(code=model.code, mdl=model.mdl)
            selected_model.save()
        except Exception as e:
            #DBで何か変なことが起きていたらもう一度入力させる
            
            return render(request, "app/index.html" ,{
            "models":MlModel.objects.all()
        })
        if "NN" in code:
            return render(request,"app/make_NN_model.html")
        else:
            return HttpResponseRedirect(reverse("datas"))
    else:
        return render(request, "app/index.html" ,{
            "models":MlModel.objects.all()
        })

def make_NN(request):
    if request.method=="POST":
        model          = NN_layers(layer1=request.POST["layer1"],layer2=request.POST["layer2"] )
        model.save()
        return HttpResponseRedirect(reverse("datas"))
    else:
        return HttpResponseRedirect(reverse("empty"))

def select_data(request):
    return render(request, "app/select_data.html")
    
def calculation(request):
    return render(request, "app/calculation.html")
                

def get_result(request):
    return render(request, "app/get_result.html")

def help(request):
    return render(request, "app/help.html")

def empty(request):
    return render(request,"tech/empty.html" )
