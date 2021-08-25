from django.contrib import admin

from .models import Movie
from .models import Director
from .models import Actor


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
