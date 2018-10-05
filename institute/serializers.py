from rest_framework  import serializers
from institute.models import Course
from institute.models import  User
class courseSerilizer(serializers.ModelSerializer):

     class Meta:
         model=Course
         fields=('__all__')


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')