from django.db import models
from variables.models import Variable


# Create your models here.
# class Formula(models.Model):
# 	name = models.CharField(max_length=100, blank=True)
# 	param1 = models.CharField(max_length=50, blank=True )
# 	express1 = models.CharField(max_length=100, blank=True)
# 	param2 = models.CharField(max_length=50, blank=True)
# 	express2 = models.CharField(max_length=100, blank=True)
# 	param3 = models.CharField(max_length=50, blank=True)
# 	express3 = models.CharField(max_length=100, blank=True)
# 	param4 = models.CharField(max_length=50, blank=True)
# 	express4 = models.CharField(max_length=100, blank=True)

class Formula(models.Model):
	name = models.CharField(max_length=100, blank=True)
	formulaID = models.IntegerField()
	inversion = models.IntegerField()
	

	def __str__(self):
		return self.name
	







