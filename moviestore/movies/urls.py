from django.urls import path
from matplotlib.pyplot import show
from . import views

urlpatterns = [
    path('',views.moviesListView.as_view(), name='movie.all'),
    path('<int:pk>', views.moviesDetailView.as_view(), name="movie.show"),
    path('<int:id>/review',views.review, name="movie.review")
]