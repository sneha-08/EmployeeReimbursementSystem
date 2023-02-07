from django.db import models


# Create your models here.

# model to get employee expense
class Expense(models.Model):
    item = models.CharField(max_length = 50)    # expense item name
    eid = models.IntegerField()                 # recorde employee id
    amount = models.IntegerField()              # expense amount
    category = models.CharField(max_length=50)  # category of the expense like food, travel, others
    date = models.DateField()                   # date of expense 
    status = models.CharField(default= "ON PROCESS",max_length=50)  # status of expense like Approved, Declined or On Process

    def __str__(self):
        return self.name