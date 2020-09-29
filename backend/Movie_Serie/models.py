from django.db import models


# Create your models here.
class Statu(models.Model):
    title = models.CharField(verbose_name="Status", max_length=40)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name="Title", max_length=40, unique=True)

    def __str__(self):
        return self.title


class Movie_or_Serie(models.Model):
    title = models.CharField(verbose_name="Movie Title", max_length=40, unique=True)
    length = models.CharField(verbose_name="Movie Length", max_length=40)
    status = models.ForeignKey(Statu, on_delete=models.CASCADE)
    imdb = models.CharField(verbose_name='IMDb', blank=True, null=True, max_length=4)
    stars = models.TextField(verbose_name="Stars")
    director = models.CharField(verbose_name="Director", max_length=80)
    total_season = models.IntegerField(verbose_name="Total Season", null=True, blank=True)
    review_img = models.TextField(verbose_name="Review Image")
    category = models.ManyToManyField(Category)
    production_year = models.CharField(max_length=4, verbose_name="Production Year")
    added_date = models.DateTimeField(auto_now_add=True)
    short_desc = models.TextField(verbose_name="Description")
    available_4k = models.BooleanField(verbose_name="4K Available", default=False, null=True, blank=True)
    available_fhd = models.BooleanField(verbose_name="FHD Available", default=False, null=True, blank=True)
    available_hd = models.BooleanField(verbose_name="HD Available", default=False, null=True, blank=True)
    slug = models.SlugField(max_length=150, verbose_name="Slug", blank=True, null=True, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


class URL(models.Model):
    movie_or_serie = models.ForeignKey(Movie_or_Serie, on_delete=models.CASCADE)
    season_number = models.IntegerField(verbose_name="Season", null=True, blank=True)
    episode_number = models.IntegerField(verbose_name="Episode", null=True, blank=True)
    link_4k = models.TextField(verbose_name="4k Link", null=True, blank=True)
    link_fhd = models.TextField(verbose_name="Full HD Link", null=True, blank=True)
    link_hd = models.TextField(verbose_name="HD Link", null=True, blank=True)

    def __str__(self):
        return self.movie_or_serie.title
