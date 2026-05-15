from django.shortcuts import render

# Create your views here.
def home(request):
    appname = "Lumière Movies"
    context = {
        "name": appname
    }
    return render(request, "index.html", context)