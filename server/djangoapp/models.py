from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    # Add any additional fields as needed

    def __str__(self):
        return self.name  # String representation of the CarMake object

# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)  # Name of the car model
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Type of car
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        default=2023
    )  # Year of the car model
    dealer_id = models.IntegerField()  # Dealer ID from the Cloudant database

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # String representation of the CarModel object
