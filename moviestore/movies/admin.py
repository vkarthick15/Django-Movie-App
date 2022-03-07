from django.contrib import admin
from .models import Review, movies

# Register your models here.
admin.site.register(movies)
admin.site.register(Review)