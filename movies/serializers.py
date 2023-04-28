from rest_framework import serializers
from movies.models import Movie, RatingMovie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(max_length=127, default=None)

    rating = serializers.ChoiceField(
        choices=RatingMovie.choices, default=RatingMovie.DEFAULT
    )
    duration = serializers.CharField(max_length=10, default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.SerializerMethodField()

    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        return MovieOrder.objects.create(**validated_data)

    def get_buyed_by(self, obj: dict):
        return obj.buyed.email
    
    def get_title(self, obj: dict):
        return obj.movies_orders.title
    
    def get_buyed_at(self, obj: dict):
        return obj.buyed_at
