from django.db import models

# Create your models here.

class Equation(models.Model):
	name = models.CharField(max_length=100,null=True)
	param = models.CharField(max_length=100, null=True)
	formulaID = models.IntegerField(null=True)
	inversion = models.IntegerField(null=True)

	

	def __str__(self):
		return self.name

