from tastypie.resources import ModelResource
from api.models import Planet
from tastypie.authorization import Authorization

class PlanetResource(ModelResource):
    class Meta:
        queryset = Planet.objects.all()
        resource_name = 'planet'
        authorization = Authorization()