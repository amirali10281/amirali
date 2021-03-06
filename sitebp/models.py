from django.db import models

# Create your models here.
class Videos(models.Model):
    name=models.CharField( max_length=50)
    file=models.FileField(upload_to="videos")
    

    def __str__ (self):
        return self.name


class Exercise (models.Model):
    name=models.CharField(max_length=50)
    file = models.FileField( upload_to="exercise")
    deadline=models.DateField( auto_now=False, auto_now_add=False,blank=True , null=True)


    def __str__ (self):
        return self.name