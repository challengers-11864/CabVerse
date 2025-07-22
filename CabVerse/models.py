from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Rider(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Driver(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    car_model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)
    car_capacity = models.PositiveIntegerField()
    license_number = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=10)
    insurance_pollution = models.BooleanField(default=False)  # True = Yes, False = No

    def __str__(self):
        return self.username

class Ride(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
    )
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rides_requested')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='rides_taken')
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    ride_type = models.CharField(max_length=10, choices=(('now', 'Now'), ('later', 'Later')), default='now')
    scheduled_time = models.DateTimeField(null=True, blank=True)
    total_passenger = models.PositiveIntegerField(help_text="Total passengers including children")
    # preferred_car_model = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.ride_type == 'later' and not self.scheduled_time:
            raise ValidationError("Scheduled time must be provided for 'later' rides.")
        if self.ride_type == 'now':
            self.scheduled_time = None

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class RiderRating(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    ride_experience = models.IntegerField()
    driver_behaviour = models.IntegerField()
    car_cleanliness = models.IntegerField()
    comfort_level = models.IntegerField()
    punctuality = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Rider Rating for {self.rider.username}"


class DriverRating(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rider_behaviour = models.IntegerField()
    punctuality = models.IntegerField()
    cleanliness = models.IntegerField()
    payment_issues = models.IntegerField()
    overall_cooperation = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Driver Rating for {self.driver.username}"
