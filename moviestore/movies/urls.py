from django.urls import path
from matplotlib.pyplot import show
from . import views

urlpatterns = [
    path('',views.index),
    path('<str:title>', views.show)
]