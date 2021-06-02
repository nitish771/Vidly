from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movies/', include('movies.urls'), name='movies'),
    # path('genres/', views.index, name='generes_index'),
]
