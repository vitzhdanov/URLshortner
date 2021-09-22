from django.db import models


class Url(models.Model):
    long_url = models.TextField()
    short_url_sym = models.URLField()
    short_url_em = models.URLField()
