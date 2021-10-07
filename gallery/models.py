from django.db import models

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to='images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =60)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    @classmethod
    def update_images(cls):
        images = cls.objects.all()
        return images       
  
    @classmethod
    def get_image_id(cls,id):
        img = cls.objects.filter(id=id)
        return img

    @classmethod
    def search_image_by_category(cls,category):
        image_category = cls.objects.filter(category=category)
        return image_category

    @classmethod
    def filter_image_by_location(cls,location):
        image_location = cls.objects.filter(location=location)
        return image_location






class Location(models.Model):
    location_name = models.CharField(max_length=60)



    def save_location(self):
        self.save()

    def __str__(self):
        return self.location_name()

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations       



class Category(models.Model):
    category_name =models.CharField(max_length=60)

    def save_category(self):
        self.save()
    def __str__(self):
        return self.category_name()
   

    @classmethod
    def get_category(cls):
        category = cls.objects.all()
        return category      

