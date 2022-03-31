from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    item_category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{}".format(self.item_category)


class Room(models.Model):
    room = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{}".format(self.room)


class Condition(models.Model):
    condition = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{}".format(self.condition)


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200, blank=True, null=True)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=100, decimal_places=2)
    date_entered = models.DateField(default=datetime.now)


