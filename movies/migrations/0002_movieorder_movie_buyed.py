# Generated by Django 4.2 on 2023-04-20 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                (
                    "buyed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users_orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movies_orders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_movies",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="buyed",
            field=models.ManyToManyField(
                related_name="users_movies",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]