from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User


class Package(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price =models.PositiveIntegerField()
    destination = models.CharField(max_length=10)
    starting_Date=models.DateField()
    duration = models.DurationField(default=timedelta(days=5))
    def __str__(self):
        return "%s" % (str(self.title))
    
    
class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="booker")#change this to one2one relation
	package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="bookings")#change this to one2one relation
	date = models.DateField(auto_now=True)
	tickets = models.PositiveIntegerField()

	def __str__(self):
		return "%s: %s booked on : %s" % (self.user.username, str(self.package),str(self.date))