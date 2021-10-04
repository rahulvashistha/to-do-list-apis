from django.db import models
from django.db.models.deletion import CASCADE
from datetime import date
# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver

from django.contrib.auth.models import User
# Create your models here.

task_category_choices = (
    ("None", "None"),
    ("Personal", "Personal"),
    ("Shopping", "Shopping"),
    ("Wishlist", "Wishlist"),
    ("Work", "Work"),
)
task_repeat_choices = (
    ("No Repeat", "No Repeat"),
    ("Once a Day", "Once a Day"),
    ("Once a Week", "Once a Week"),
    ("Once a Month", "Once a Month"),
    ("Once a Year", "Once a Year"),
)
task_status_choices = (
    ("Not Completed", "Not Completed"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
)

class Task(models.Model):
    task_title = models.CharField(max_length=30, null=False)
    task_content = models.TextField(max_length=100)
    task_content = models.TextField(max_length=100)
    
    task_added_date = models.DateField(blank=True)
    task_due_date = models.DateField(blank=True)
    task_due_time = models.TimeField(blank=True)
    #task_completion_time = models.DateTimeField(blank=True)
    
    task_category = models.CharField(max_length=15, choices=task_category_choices, default="None")
    task_repeat = models.CharField(max_length=15, choices=task_repeat_choices, default="No Repeat")
    task_status = models.CharField(max_length=15, choices=task_status_choices, default="Not Completed")


    def __str__(self):
        return self.task_title + ' In ' + self.task_category 