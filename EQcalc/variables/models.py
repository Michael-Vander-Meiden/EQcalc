from django.db import models

# Create your models here.
class Variable(models.Model):
	name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=100)
	value = models.IntegerField(default = 0)

