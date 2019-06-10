# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=50)
    body = models.TextField()
    img = models.URLField(max_length=2000000, blank='True')

    def __str__(self):
        return self.title
