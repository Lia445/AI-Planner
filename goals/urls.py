from django.urls import path
from . import views

urlpatterns = [
    path('create_plan/', views.create_plan, name="create_plan"),
    path('plans/', views.plans, name="plans"),
    path('view_plan/<int:id>', views.view_plan, name="view_plan"),
]