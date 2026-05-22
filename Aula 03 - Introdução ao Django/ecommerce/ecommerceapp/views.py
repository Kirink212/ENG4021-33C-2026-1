from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    appname = "Lumière Movies"
    movies = Movie.objects.select_related("director").all()
    # for movie in movies:
    #     print(movie.title)
    
    context = {
        "name": appname,
        "movies": movies
    }
    return render(request, "index.html", context)

def create_movie(request):
    form = MovieForm()
    context = {
        "form": form
    }
    return render(request, "movie_form.html", context)