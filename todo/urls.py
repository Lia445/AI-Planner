from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('view_task/<int:id>', views.view_task, name="view_task"),
    path('update/<int:id>', views.update, name="update"),
    path('next_status/<int:id>', views.next_status, name="next_status"),
    path('delete/<int:id>', views.delete, name="delete"),
]