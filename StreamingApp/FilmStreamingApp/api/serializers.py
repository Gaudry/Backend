from rest_framework import serializers
from ..models import FilmsApplication


class FilmStreamingAppSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = FilmsApplication
        fields = ('name', 'director', 'description', 'image', 'liked_yes_or_no', 'seen_yes_or_no')
        #fields = ('name', 'director', 'description', 'image')

class SearchedFilmSerializer(serializers.Serializer):
    Category = serializers.CharField()
    ID = serializers.CharField()
    Image = serializers.ImageField()
    Movie_Title = serializers.CharField()
    Rank = serializers.ImageField()