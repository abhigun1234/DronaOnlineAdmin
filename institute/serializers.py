from rest_framework  import serializers
from institute.models import Course
from institute.models import  User
from django.db.models import Q
class courseSerilizer(serializers.ModelSerializer):

     class Meta:
         model=Course
         fields=('__all__')


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course

class userLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')

    def validate(self, data):
        user_obj=None
        email=data.get("email",None)
        name=data.get("name",None)
        password=data["password"]
        if not email  or name:
            raise  ValueError("A username or mail  is required to login")
        user =User.objects.filter(Q(email=email)|Q(name=name)).distinct()

        if user.exists() and user.count() ==1:
            user_obj=user_obj.first()
        else:
            raise SyntaxError
        if user_obj:
            if not  user_obj.checkPassword(password):
                pass
        return data