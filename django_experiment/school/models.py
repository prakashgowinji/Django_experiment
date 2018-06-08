# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Library(models.Model):
    librarian = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.librarian)

class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    price = models.CharField(max_length=10)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
