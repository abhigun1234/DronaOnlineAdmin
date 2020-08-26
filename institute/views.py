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
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .models import Course
#serilizer used for converting the the data into json
from .serializers import courseSerilizer,userSerializer
from .models import  User



#class course details returns the  course list and add the course into database


class courseDetails(APIView):

    def get(self,request):
        courses=Course.objects.all()
        print(courses)
        serilezer=courseSerilizer(courses,many=True)
        return Response({'courseDetails': serilezer.data})
    def post(self,request):
        print(request.data)
        try:
            courseData=request.data
            name=courseData['name']
            fees=courseData['fees']
            duration=courseData['duration']
            description = courseData['description']
            imageUrl=courseData['imageUrl']
            videoUrl = courseData['videoUrl']
            course=Course(name=name,fees=fees,duration=duration,description=description,videoUrl=videoUrl)
            course.save()
            return Response("course added")

        except:
            return "error"



'''
class User defines the drona online user register and login  functionlity

'''
class RegisterUser(APIView):
    def get(self,request):

        users = User.objects.all()
        print(users)
        serilezer = userSerializer(users, many=True)
        return Response({'userdetails': serilezer.data})

    def post(self,request):

        print(request.data)
        userData=request.data
        response=''

        try:
                name=userData['name']
                print(name)
                phone_no=userData['phone_no']
                city=userData['city']
                country=userData['country']
                email=userData['email']
                birth_date=userData['birth_date']
                # Python code to illustratdde Sending mail from
                # your Gmail account
                print(request.json)
                import smtplib

                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                # start TLS for security
                s.starttls()
                s.ehlo()
                # Authentication
                s.login("justolearnpune@gmail.com", "justo.007")

                # message to be sent
                message = "Message_you_need_to_send"

                # sending the mail
                s.sendmail("nitesh.aryan007@gmail.com", "nitesh.aryan007@gmail.com", message)

                # terminating the session
                s.quit()
                user=User(name=name,phone_no=phone_no,city=city,email=email,birth_date=birth_date)
                user.save()
                response='registerd'
                return Response(response)
        except:
                response = 'error'
                return Response(response)


class UserLoginApiView(APIView):
    permission_classes = []

    def post(self, request):
        print(request.data)
        userData = request.data
        serilezer = userSerializer(userData, many=True)
        if serilezer.is_valid(raise_exception=True):
            pass

