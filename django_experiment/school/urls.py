from django.conf.urls import url
from . import views

app_name='books'

urlpatterns = [
    url(r"^$", views.BookList.as_view(), name="all"),
    url(r"new/$", views.CreateBook.as_view(), name="create"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteBook.as_view(),name="delete"),
]
