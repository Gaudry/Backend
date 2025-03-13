from django.urls import path
from ..api import views

urlpatterns = [
    #Films
    path("films/", views.FilmAppViewset.as_view()),
    path("film/<int:film_id>/", views.SingleFilmAppViewset.as_view(), name='film_id'),
    path("search/<str:film_title>/", views.SearchFilmsbyCategoryMovie.as_view(), name='film_title'),
    path("searchbyid/<str:film_id>/", views.SearchFilmsbyId.as_view(), name='film_id'),
    path("analysisandrecommendationsbyid/<str:film_id>/", views.GetFillmsAnalysisAndRecomendationsbyId.as_view()),
    path("listoffilms/", views.GetFilmsFromRapidApi.as_view(), name='film_list'),

    #
    path("city/<str:city>/", views.CityWeatherApp.as_view(), name='city'),

    #
    path("ip/", views.IpAdress.as_view()),
]