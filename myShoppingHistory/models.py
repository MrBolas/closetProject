from django.db import models

# Create your models here.

class Item(models.Model):

    timeStamp= models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField(default=1)

    #def __init__(self, title, description, quantity):
    #    self.title = models.CharField(max_length=200)
    #    self.description = models.TextField()
    #    self.quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def printValues(self):
        print(self.title)
        print(self.description)
        print(self.quantity)
