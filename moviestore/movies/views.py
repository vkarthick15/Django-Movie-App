from hashlib import new
from pyexpat import model
from re import template
from unicodedata import name
from django.shortcuts import render,get_object_or_404,redirect
from matplotlib.style import context
from .models import movies,Review
from django.views.generic import ListView,DetailView
import json

moviesdata = open('D:\Programming\Django\moviestore\movie.json').read()
data = json.loads(moviesdata)

# Create your views here.

class moviesListView(ListView):

    def get_queryset(self):
        return movies.objects.all()

#generic list view makes the codes of lines less and therefore easy to understand, here moviesListView and index function perform the same tasks
# def index(request):
#      dbdata = movies.objects.all()
#      context = {'movies': dbdata}
#      return render(request, 'movies\index.html', context)


class moviesDetailView(DetailView):
     #      reviews = Review.objects.filter(book_id=id).order_by('-created_at')
     template_name = "movies\movies_detail.html"
     model = movies
     context_object_name = 'movie'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs) 
          context['reviews'] = context['movie'].review_set.order_by('-created_at')
          return context


# def show(request,id):
#      singlemovie =  get_object_or_404(movies,pk=id)
#      reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#      context = {'movie':singlemovie, 'reviews': reviews}
#      return render(request, 'movies\show.html', context)

def review(request,id):
     body = request.POST['review']
     newreview = Review(body=body,movie_id=id)
     newreview.save()
     return redirect(f"/movie/{id}")