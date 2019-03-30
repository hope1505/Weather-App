from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
        
#class Contact(models.Model):
 #   contact_name = models.CharField(max_length=25)
  #  contact_email = models.EmailField()
   # contact_content = models.CharField(max_length=100)
    
    #def __str__(self):
     #   return self.name
