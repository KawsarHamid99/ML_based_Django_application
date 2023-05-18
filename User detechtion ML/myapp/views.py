from django.shortcuts import render, redirect,HttpResponse
from .models import Video

# Create your views here.
def home(request):
    return render(request,"home.html")


from joblib import load
model=load("model.joblib")

def result(request):
    name=""
    if request.method=="POST":
        sepal_length=request.POST.get("sepal_length")
        sepal_width=request.POST.get("sepal_width")
        petal_length=request.POST.get("petal_length")
        petal_width=request.POST.get("petal_width")
        print("-----------------------------------")
        print(sepal_length,sepal_width,petal_length,petal_width )
        y_pred=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        #print(y_pred)
        if y_pred[0]== 0:
            y_pred="setosa"
        if y_pred[0]== 1:
            y_pred="versicolor"
        if y_pred[0]== 2:
            y_pred="virginica"
        print(y_pred)
    return render(request,"result.html",{"name":y_pred})


