from rest_framework  import serializers
from institute.models import Course
from institute.models import  user
class courseSerilizer(serializers.ModelSerializer):

     class Meta:
         model=Course
         fields=('__all__')


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('__all__')


class userLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=('__all__')