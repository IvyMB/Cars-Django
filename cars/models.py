from django.db import models

# Create your models here.

class Brand (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.id} - {self.name}'
    

class Car (models.Model):
     id = models.AutoField(primary_key=True)
     model = models.CharField(max_length=200)
     brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars_brand')
     factory_year = models.IntegerField(blank=True, null=True)
     brand_year = models.IntegerField(blank=True, null=True)
     plate = models.CharField(max_length=200, blank=True, null=True)
     value = models.FloatField()
     photo = models.ImageField(upload_to='cars/medias', blank=True, null = True)
     
     def __str__(self):
         return self.model
     