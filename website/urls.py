from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path ('register/', views.registerUser, name='register'),
    path ('record/<int:pk>', views.customerRecord, name='record'),
    path ('delete_record/<int:pk>', views.deleteRecord, name='deleteRecord'),
    path ('add_record/', views.addRecord, name='addRecord'),
    path ('update_record/<int:pk>', views.updateRecord, name='updateRecord'),
    
    
]
