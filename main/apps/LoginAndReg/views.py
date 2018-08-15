from django.shortcuts import render, HttpResponse, redirect
#import for random word
from django.utils.crypto import get_random_string
#import for time thing
from time import gmtime, strftime
def index(request):
    context = {
        "message" : "Smoke grass and eat ass!",
        "for" : "The Children",
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "LoginAndReg/Home.html", context)
#rendom word and redirect
def word(request):
    context = {"word": get_random_string(length = 14)}
    return render(request, "LoginAndReg/Random.html", context)

def refresh(request):
    return redirect(word)

#form test
def survey(request):
    return render(request, "LoginAndReg/Survey.html")

def submit(request, methods = "POST"):
    print request.POST["name"]
    #print request.POST["desc"]
    if(methods == "POST"):
        request.session['name'] = request.POST['name']
        request.session['desc'] = request.POST['desc']
    return redirect("/result")

def result(request):
    return render(request, "LoginAndReg/Result.html")
    