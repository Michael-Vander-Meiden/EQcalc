from django.contrib import admin
from .models import Equation, Variable, Units

# Register your models here.

admin.site.register(Equation)
admin.site.register(Variable)
admin.site.register(Units)