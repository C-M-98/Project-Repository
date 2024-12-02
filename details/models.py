from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Styles(models.Model):
    description = models.CharField(max_length=255)
    image = ImageField()
    profile_image = ImageField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    image = ImageField()
    title = models.CharField(blank=True,max_length=100)
    description = models.CharField(max_length=255)
    text_field = models.CharField(max_length=1500 ,blank=True)
    
    def __str__(self):
        
        return self.title
    
class Education(models.Model):
    organisation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    certificate = ImageField()
    def __str__(self):
        return self.organisation
class EduStyles(models.Model):
    title = models.CharField(max_length=100)
    image = ImageField();
    def __str__(self):
       return self.title 
   
class About(models.Model):
    name= models.CharField(max_length=100);
    about= models.CharField(max_length=255);
    
    def __str__(self):
        return self.name