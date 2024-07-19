from django.db import models
class Itemlist(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    discount=models.FloatField()
    def __str__(self):
        return self.name  
    
# Create your models here.
