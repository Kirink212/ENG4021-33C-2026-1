from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        form =  MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    context = {
        "form": form
    }
    return render(request, "movie_form.html", context)

def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == "POST":
        form =  MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm(instance=movie)
    context = {
        "form": form
    }
    return render(request, "movie_form.html", context)

def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        confirm = request.POST.get("confirm")
        if confirm == "Sim":
            movie.delete()
        return redirect('home')
    
    context = {"movie": movie}
    return render(request, "delete_movie.html", context = context)