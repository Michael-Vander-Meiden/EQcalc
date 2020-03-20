from django.db import models

# Create your models here.

class Equation(models.Model):
	name = models.CharField(max_length=100, blank=True)
	formulaID = models.IntegerField(blank = True)
	inversion = models.IntegerField(blank = True)
	

	def __str__(self):
		return self.name