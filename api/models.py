from django.db import models
from django.utils import timezone
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
    
    def dehydrate(self, bundle):
        bundle.data['Added'] = timezone.now()
        return bundle

        