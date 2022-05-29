from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Clas(models.Model):
    name = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    def __str__(self):
        return self.name


class Reservation(models.Model):
    clas = models.OneToOneField(Clas, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.clas} <=> {self.club}"


