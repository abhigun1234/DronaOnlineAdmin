from rest_framework  import serializers
from institute.models import Course
class courseSerilizer(serializers.ModelSerializer):

     class Meta:
         model=Course
         fields=('__all__')