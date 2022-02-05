from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return super().__str__()
class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return super().__str__()


class Site(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=200)
    justification = models.TextField(max_length=200,default="")
    year = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region, on_delete=CASCADE,null=True)
    iso = models.ForeignKey(Iso, on_delete=CASCADE,null=True)

    
    
    longitude = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    area_hectares = models.FloatField(null=True,blank=True)

    
    def __str__(self) :
        return self.name