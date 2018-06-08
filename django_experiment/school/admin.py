# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from .models import Library, Book

# Register your models here.
admin.site.register(Library)
admin.site.register(Book)
