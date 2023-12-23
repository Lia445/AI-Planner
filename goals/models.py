from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    name = models.CharField(max_length=50, default=None)
    objective = models.TextField(default=None)
    max_date = models.DateField(default=None)
    weekly_hours = models.IntegerField(default=None)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['max_date']
        
        


    


