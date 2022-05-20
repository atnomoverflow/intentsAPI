from http.client import responses
from rest_framework import  serializers
from intents.models import Intents 
# Serializers define the API representation.
class IntentsWithoutIDSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = Intents
        fields = ['tag','patterns','responses']
class IntentsSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = Intents
        fields = ['id','tag','patterns','responses']