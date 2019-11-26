from django.db import models


class Category(models.Model):
    gender= models.CharField(max_length=50)


    def __str__(self):
        return self.gender

class product(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    price = models.FloatField()
    image = models.ImageField(upload_to='pics')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
