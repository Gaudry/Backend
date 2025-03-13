from django.contrib.auth.views import LoginView
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, response
from rest_framework.permissions import IsAuthenticated
from ..models import *
from datetime import datetime, timedelta
from django.utils import timezone
import jwt, datetime

# serilaizer
from .serializers import MultimediaSerializer, SingleMultimediaSerializer

import logging
#########
import socket


log = logging.getLogger(__name__)

def GetUserDeviceInfos():

    return {'ip': socket.gethostbyname(socket.gethostname()), 'hostname': socket.gethostname()}

class AddMultimedia(APIView):
    def post(self, request, *args, **kargs):
        request_data = {**request.data}
        serializer = MultimediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = {
                'success': True,
                'mult': serializer.data
            }

            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(
            serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)

class GetMultimedia(APIView):
    def get(self, request, section):
        sct = section.lower()[0].upper() + section.lower()[1:]
        try:
            objects = Multimedia.objects.filter(section_multimedia_type=sct)
            context = {'request': request}
            results = SingleMultimediaSerializer(objects, many=True, context=context).data

            return Response(results)

        except Exception as ex:

            log.error( f"***** exception {ex}")
            return Response(None)