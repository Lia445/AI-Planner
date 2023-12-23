from django.forms import ModelForm
from .models import Plan

class CreatePlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'objective', 'max_date', 'weekly_hours']
        help_texts = {
            "max_date": "Format: YYYY-MM-DD",
        }     
           
        
        
# I would like to plan a trip to France. The duration of the trip is going to be 1 month and during that time I will do voluntary work at a hostel in exchange for acomodation. In the weekends I would like to visit the main tourist atractions, especially focusing on ecoturism, and go to the best restaurants. The maximum budget for this trip is 10000 dollars and I would like some tips to save that money.