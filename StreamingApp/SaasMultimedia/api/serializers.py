from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.authtoken.models import Token

from datetime import datetime, timedelta
from django.utils import timezone

from ..models import *


class MultimediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multimedia
        fields = '__all__'

class SingleMultimediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multimedia
        fields = ["image", "alt", "title"]