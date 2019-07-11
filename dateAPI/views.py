from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import throttle_classes
import time as t
# Create your views here.


@api_view(['GET'])
# considering anonymous user and particular user both.
@throttle_classes([AnonRateThrottle, UserRateThrottle])

def get(request, format=None):
	return Response(t.ctime())