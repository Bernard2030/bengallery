from django.db import models

# Create your models here.
class Image(models.Model):
    Image= models.ImageField(upload_to='images/')
    Name = models.CharField(max_length =30)
    Description = models.CharField(max_length =60)
    Location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(category,on_delete=models.CASCADE,default=None)