from django.shortcuts import render
from intents.serializers import IntentsWithoutIDSerializer,IntentsSerializer
from intents.models import Intents
from rest_framework import viewsets
# Create your views here.
class IntentsViewSet(viewsets.ModelViewSet):
    queryset = Intents.objects.all()
    serializer_class = IntentsWithoutIDSerializer
    def get_serializer(self, *args, **kwargs):
        # add many=True if the data is of type list
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(IntentsViewSet, self).get_serializer(*args, **kwargs)
class IntentsIDViewSet(viewsets.ModelViewSet):
    queryset = Intents.objects.all()
    serializer_class = IntentsSerializer
    def get_serializer(self, *args, **kwargs):
        # add many=True if the data is of type list
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(IntentsIDViewSet, self).get_serializer(*args, **kwargs)