from django.db import models
from goals.models import Plan
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=50, default=None)
    description = models.TextField(null= True, blank=True)
    date = models.DateField(default=None)
    hours = models.FloatField(null=True, blank=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE) 
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE, null=True, blank=True)
    
    class StatusChoices(models.TextChoices):
        not_started = "NOT STARTED"
        doing = "DOING"
        done = "DONE"
        
    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.not_started,
        max_length=12,
    )
     
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['status']