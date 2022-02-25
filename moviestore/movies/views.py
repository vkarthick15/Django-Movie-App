from unicodedata import name
from django.shortcuts import render
from matplotlib.style import context
import json

moviesdata = open('D:\Programming\Django\moviestore\movie.json').read()
data = json.loads(moviesdata)

# Create your views here.

def index(request):
     context = {'movies':data}
     return render(request, 'movies\index.html', context)

def show(request,id):
     singlemovie = list()
     for movie in singlemovie:
          if movie['id'] == id:
               singlemovie = movie
     context = {'movie':singlemovie}
     return render(request, 'movies\show.html', context)