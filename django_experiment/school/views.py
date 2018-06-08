# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.shortcuts import render
from . import forms
from . import models
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

from django.contrib.auth import get_user_model
User = get_user_model()


class BookList(SelectRelatedMixin, generic.ListView):
    model = models.Book
    select_related =  ("library", "library")

class CreateBook(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Book

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CreateBook, self).form_valid(form)


class DeleteBook(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Book
    select_related = ("title", "author")
    success_url = reverse_lazy("books:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Book Deleted")
        return super(DeleteBook, self).delete(*args, **kwargs)
