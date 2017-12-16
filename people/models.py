# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
   person_name = models.CharField(max_length=300)
   person_age = models.IntegerField()

class Books(models.Model):
   pname = models.ForeignKey(Person, on_delete=models.CASCADE)
   book_name = models.CharField(max_length=400)


