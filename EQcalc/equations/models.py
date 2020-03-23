from django.db import models

# Create your models here.

class Equation(models.Model):
	name = models.CharField(max_length=100,)
	formulaID = models.IntegerField()
	inversion = models.IntegerField()
	

	def __str__(self):
		return self.name