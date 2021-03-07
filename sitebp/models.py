from django.db import models
from datetime import datetime  

# Create your models here.
class Videos(models.Model):
    name=models.CharField( max_length=300)
    file=models.FileField(upload_to="videos")
    

    def __str__ (self):
        return self.name


class Exercise (models.Model):
    name=models.CharField(max_length=300)
    file = models.FileField( upload_to="exercise")
    deadline=models.DateTimeField( auto_now=False, auto_now_add=False ,null=True,blank=True)
    #date=models.DateField( auto_now=False, auto_now_add=False,null=True,blank=True)

    def __str__ (self):
        return self.name

class Answers (models.Model):
    exercise=models.ForeignKey("Exercise", on_delete=models.CASCADE, null=True)
    number=models.IntegerField()
    file = models.FileField( upload_to="exercise")
    deadline= models.DateTimeField(default=datetime.now(), blank=True)
    vote=models.IntegerField(default=100)

    def __str__ (self):
        return str(self.number)