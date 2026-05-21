from django.db import models
from django.contrib.auth.models import User

class HajjService(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    camp_location = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class PilgrimProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50)
    identity_number = models.CharField(max_length=20) 
    identity_type = models.CharField(
        max_length=10, 
        choices=[('National', 'National ID'), ('Passport', 'Passport')],
        default='National'
    )
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    def __str__(self):
        return self.user.username

class Booking(models.Model):
    pilgrim = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(HajjService, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pilgrim.username} -> {self.service.title}"