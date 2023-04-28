from django.db import models


class RatingMovie(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None)

    rating = models.CharField(
        max_length=20, choices=RatingMovie.choices, default=RatingMovie.DEFAULT
    )
    synopsis = models.TextField(default=None, null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    buyed = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="users_movies",
    )


class MovieOrder(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    buyed_at = models.DateTimeField(auto_now_add=True)

    buyed = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="users_orders"
    )

    movies_orders = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="orders_movies"
    )
