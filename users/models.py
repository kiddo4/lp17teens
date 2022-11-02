from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	Firstname=models.CharField(max_length=100)
	Lastname=models.CharField(max_length=100)
	Zone=models.CharField(max_length=100)
	def __str__(self):
		return self.Lastname
		

		
		
# Create your models here.

