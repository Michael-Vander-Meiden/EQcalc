from django.db import models

# Create your models here.


class Units(models.Model):
	name = models.CharField(max_length=100,null=True)
	unitConversion = models.FloatField(null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "units"

	
	


class Variable(models.Model):
	name = models.CharField(max_length=100,null=True)
	numerator = models.ManyToManyField(Units, related_name='numerator')
	denominator = models.ManyToManyField(Units, related_name='denominator')
	

	
	def __str__(self):
		return self.name


class Equation(models.Model):
	name = models.CharField(max_length=100,null=True)
	inputs = models.ManyToManyField(Variable, related_name = 'inputs')
	param = models.ForeignKey(Variable, null=True, on_delete=models.SET_NULL)
	formulaID = models.IntegerField(null=True)
	inversion = models.IntegerField(null=True)

	

	def __str__(self):
		return self.name
