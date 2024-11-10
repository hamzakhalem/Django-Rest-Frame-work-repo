from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters

# Create your views here.
#1 without REST and no model query FBV
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            "Name": "Omar",
            "mobile": 789456,
        },
        {
            'id': 2,
            'name': "yassin",
            'mobile': 74123,
        }
    ]
    return JsonResponse (guests, safe=False)

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name','mobile'))
    }
    return JsonResponse(response)


def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)