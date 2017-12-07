from django.db import models
from django.core.urlresolvers import reverse

class Actual(models.Model):
    actual_rns = models.FloatField()
    actual_arr = models.FloatField()
    actual_rev = models.FloatField()