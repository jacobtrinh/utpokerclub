from django.db import models

# Create your models here.

class Host(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=16)
    email = models.CharField(max_length=200)
    phone_number = models.FloatField()

    def __str__(self):
        return self.name

class Home_Game(models.Model):
    host = models.ForeignKey(Host, null=True, on_delete=models.SET_NULL)
    stake = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.host:
            return self.host.name + " Home Game"
        return "?"

class Member(models.Model):
    name = models.CharField(max_length=16)
    phone_number = models.FloatField()
    year = models.CharField(max_length=16)
    age = models.IntegerField()

class Contact(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject =models.TextField(default="No Subject", blank=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"




