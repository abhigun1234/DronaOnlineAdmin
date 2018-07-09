from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
@api_view(['GET', 'POST'])
def dronahome(request):
    return render(request,'home.html')

