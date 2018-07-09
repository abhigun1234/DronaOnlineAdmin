from django.shortcuts import render
# HttpResponse is used to return response
from django.http import HttpResponse
#not found
from django.shortcuts import get_object_or_404
#returns the api data
from rest_framework.views import APIView
# returns response like 200 ok 404
from rest_framework.response import Response
from  rest_framework  import status  #return status
from .models import Course
#serilizer used for converting the the data into json
from .serializers import courseSerilizer



#class course details returns the  course list and add the course into database


class courseDetails(APIView):
    def get(self,request):
        courses=Course.objects.all()
        print(courses)
        serilezer=courseSerilizer(courses,many=True)
        return Response({'courseDetails': serilezer.data})
    def post(self):
        pass