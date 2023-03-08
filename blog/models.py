from django.db import models

# Create your models here.
class Flower(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(null=True)
    price=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.name