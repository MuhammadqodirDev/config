from rest_framework import serializers
from .models import *





class Aboutserializers(serializers.ModelSerializer):
    
    class Meta:
        model = About
        fields = ('__all__')
        
        
class Productserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ('__all__')
        

class Videoserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ('__all__')
        
        
class Feedbackserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Client_feedback
        fields = ('__all__')
        
        
class Informationserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Information
        fields = ('__all__')
        

class Causeserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cause
        fields = ('__all__')