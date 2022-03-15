from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view 
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.



@api_view(['GET'])
def about_api(request):
    queryset = About.objects.all().order_by('-id')[:3]
    serialiser = Aboutserializers(queryset, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def product_api(request):
    queryset = Products.objects.all().order_by('-id')[:3]
    serialiser = Productserializers(queryset, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def video_api(request):
    queryset = Video.objects.last()
    serialiser = Videoserializers(queryset, many=False)
    return Response(serialiser.data)


@api_view(['GET'])
def feedback_api(request):
    queryset = Client_feedback.objects.all().order_by('-id')[:6]
    serialiser = Feedbackserializers(queryset, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def infor_api(request):
    queryset = Information.objects.all().order_by('-id')[:3]
    serialiser = Informationserializers(queryset, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def cause_api(request):
    queryset = Cause.objects.all().order_by('-id')[:3]
    serialiser = Causeserializers(queryset, many=True)
    return Response(serialiser.data)



import requests

def send_number(request):
    if request.method == 'GET':
        number = request.GET.get('number')
        text = number
        url = "https://api.telegram.org/bot5194823960:AAH_g0pUBHdS_11xGXoyJRDzLcsErQjidiI/sendMessage?chat_id="
        chat_id = Chat_id.objects.all()
        for id in chat_id:
            requests.get(url+str(id.id_number)+'&text='+text)
        return redirect('http://127.0.0.1:5500/index.html')