from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FilmStreamingAppSerializer, SearchedFilmSerializer
from ..models import FilmsApplication
import requests
import json
import logging
#########
import socket
from datetime import datetime
import random
import time
#############
import os
from django.conf import settings
import asyncio

from .functions import *


log = logging.getLogger(__name__)

class FilmAppViewset(APIView):

    def get(self, request):
        try:
            allfilms = FilmsApplication.objects.all()
            context = {'request': request}
            results = FilmStreamingAppSerializer(allfilms, many=True, context=context).data
            print(f"all films : {allfilms}")
            print(f"all films results: {results}")
            log.error(f"results: {results}")
            log.info(f"results: {results}")
            log.warning(f"results: {results}")
            log.debug(f"results: {results}")

            return Response(results)

        except Exception as ex:

            log.error( f"***** exception {ex}")
            log.error(f"***** exception: {results}")
            log.info(f"***** exception: {results}")
            log.warning(f"***** exception: {results}")
            log.debug(f"***** exception: {results}")
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):

        log.error(f"***** exception {request.data}")
        log.error(f"***** exception: {request.data}")
        log.info(f"***** exception: {request.data}")
        log.warning(f"***** exception: {request.data}")
        data = request.data
        #data["liked_yes_or_no"] = False
        #data["seen_yes_or_no"] = False
        print("????????????????????????????????")
        print(f"***** exception: {data}")
        print("****************************+****")
        film_serializer = FilmStreamingAppSerializer(data=data)
        #log.error(f"***** exception33333: {film_serializer}")
        print(f"***** iqwuiweqheiuewh: {film_serializer}")
        print(f"***** iqwuiweqheiuewh: {film_serializer.is_valid()}")
        print("888888888888888888888888")
        if not film_serializer.is_valid():
            log.error(f"***** exception11111: {request.data}")
            film_serializer.save()
            log.error(f"***** exception222: {request.data}")
            return Response(film_serializer.data, status=status.HTTP_201_CREATED)
        return Response(film_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleFilmAppViewset(APIView):

    def get(self, request, film_id):

        try:
            singlefilm = FilmsApplication.objects.filter(pk=id)
            context = {'request': request}
            results = FilmStreamingAppSerializer(singlefilm, many=True, context=context).data
            print("++++++++++")
            print(results)
            print("++++++++++")
            log.error(f"single film results {results}")
            return Response(results[0])

        except Exception as ex:
            log.error( f"ConsumerChapters Exception {ex}" )
            return Response(None)

    def delete(self, request, film_id):

        try:
            singlefilm = FilmsApplication.objects.get(pk=film_id).delete()
            #context = {'request': request}
            #results = FilmSerializer(singlefilm, many=True, context=context).data
            #results.delete()
            print("++++++++++")
            print(singlefilm)
            print("++++++++++")
            log.error(f"single film results {singlefilm}")
            return Response(singlefilm)

        except Exception as ex:
            #log.error( f"ConsumerChapters Exception {ex}" )
            return Response(None)

class GetFilmsFromRapidApi(APIView):

    def get(self, request):
        url = settings.API_HOST_GETFILMS_URL

        headers = {
            "x-rapidapi-key": settings.USER_API_KEY,
            "x-rapidapi-host": settings.API_HOST_GETFILMS
        }

        response = requests.get(url, headers=headers)
        print(type(response.json()))
        print(len(response.json()))
        b = random.sample(response.json(), 12)
        print("++++++++++++")
        print(b)
        print("++++++++++++")
        return Response(b)

class SearchFilmsbyCategoryMovie(APIView):

    def get(self, request, film_title):

        try:
            print(film_title)
            url = "https://cinema-api.p.rapidapi.com/get_ids/%s/movies"%(film_title)
            print(url)
            print(settings.USER_API_KEY)
            print(settings.API_HOST_SEARCH)
            headers = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": settings.API_HOST_SEARCH
            }

            response = requests.get(url, headers=headers)
            print(f"dsbsdb {response}")
            serializer = SearchedFilmSerializer(data=response.json())
            print(f"klgerjg {serializer.is_valid()}")
            return Response(response.json())

        except Exception as ex:
            return Response({"Not found object"}, status=status.HTTP_204_NO_CONTENT)

class SearchFilmsbyId(APIView):

    def get(self, request, film_id):

        try:
            print(film_id)
            url = "https://"+settings.API_HOST_FILM_ID
            print(url)
            #querystring = {"i": "tt0073195"}
            querystring = {"i": film_id}

            headers = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": "mdblist.p.rapidapi.com"
            }

            print(settings.USER_API_KEY)
            print(settings.API_HOST_FILM_ID)
            headers = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": settings.API_HOST_FILM_ID
            }

            response = requests.get(url, headers=headers, params=querystring)

            print(response.json()['title'])
            return Response(response.json())

        except Exception as ex:
            return Response({"Not found object"}, status=status.HTTP_204_NO_CONTENT)

class GetFillmsAnalysisAndRecomendationsbyId(APIView):

    def get(self, request, film_id):

        try:
            # record start time
            start = time.time()
            print(film_id)
            url = "https://" + settings.API_HOST_FILM_ID
            print(url)
            # querystring = {"i": "tt0073195"}
            querystring = {"i": film_id}

            headers = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": "mdblist.p.rapidapi.com"
            }

            print(settings.USER_API_KEY)
            print(settings.API_HOST_FILM_ID)
            headers = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": settings.API_HOST_FILM_ID
            }

            response = requests.get(url, headers=headers, params=querystring)
            #film_name
            print(response.json()['title'])

            url1 = "https://ai-movie-recommendations-reviews-suggestions-api.p.rapidapi.com/analyzeSimilarMovies"
            querystring1 = {"noqueue": "1"}
            payload1 = {
                "movieTitle": response.json()['description'],
                "lang": asyncio.run(detect_languages(response.json()['description'])).lang,
            }

            headers1 = {
                "x-rapidapi-key": settings.USER_API_KEY,
                "x-rapidapi-host": settings.API_HOST_ANALYSIS,
                "Content-Type": "application/json"
            }
            print(settings.API_HOST_ANALYSIS)
            response1 = requests.post(url1, json=payload1, headers=headers1, params=querystring1)

            print(response1.json())
            # record end time
            end = time.time()
            print("The time of execution of above program is :",
                  (end - start) * 10 ** 3, "ms")
            return Response(response1.json())

        except Exception as ex:
            return Response({"Not found object"}, status=status.HTTP_204_NO_CONTENT)

class CityWeatherApp(APIView):
    def get(self, request, city):
        api_key="3d25b28698e94b125745839fa52e1eb2"
        url1 = "https://api.openweathermap.org/geo/1.0/direct?q=%s&appid=%s"% (city, api_key)

        response = requests.get(url1)
        data = json.loads(response.text)

        url2 = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s" % (
        data[0]['lat'], data[0]['lon'], api_key)

        response2 = requests.get(url2)
        data2 = json.loads(response2.text)
        return Response(data2)

class IpAdress(APIView):
    def get(self,request):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        now = datetime.now()
        return Response({'ip1': local_ip, 'ip2': hostname, 'date': now})