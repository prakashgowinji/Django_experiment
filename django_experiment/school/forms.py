from django import forms

from school import models


class BookForm(forms.ModelForm):
    class Meta:
        fields = ("title", "author")
        model = models.Book

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["library"].queryset = (
                models.Group.objects.filter(
                    pk__in=user.groups.values_list("library__pk")
                )
            )
