from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource

from .views import home

movie_resource = MovieResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movies/', include('movies.urls'), name='movies'),
    path('api/', include(movie_resource.urls), name='api'),
]
