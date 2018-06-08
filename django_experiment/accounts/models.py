from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
#from django.core.validators import MaxValueValidator

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class Employee(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s " % self.user.username

#One to One Relationships

class Place (models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s" % self.name

class Company(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hardware_solutions = models.BooleanField(default=False)
    serves_network_solutions = models.BooleanField(default=False)

    def __str__(self):
        return "%s " % self.place.name

class Security(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s at %s" % (self.name, self.company)


#
# class Employee(models.Model):
#     #user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)
#     mobile = models.IntegerField()
#     dob = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now=True)


#Many to One Relationships

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


#Many to Many Relationships
#In this example, an Post can be published in multiple Publication objects, and a Publication has multiple Post objects
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Post(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
