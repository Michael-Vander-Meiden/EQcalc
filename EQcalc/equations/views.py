from django.shortcuts import render

from variables.models import Variable
from .models import Equation

# Create your views here.

def index(request, **kwarg):


	context = kwarg
	if 'eq' in kwarg and 'inv' in kwarg:
		eq = kwarg['eq']
		inv = kwarg['inv']
		eqlist = Equation.objects.filter(formulaID=eq)
		invlist = Equation.objects.filter(inversion=inv,formulaID=eq)
	elif 'eq' in kwarg and 'inv' not in kwarg:
		eq = kwarg['eq']
		eqlist = Equation.objects.filter(formulaID=eq)
		invlist =[]
	else:
		eqlist = []
		invlist = []

	values = []
	one = request.GET.get('1', 'empty')
	two = request.GET.get('2', 'empty')
	
	formulaID = int(request.GET.get('formulaID', False))
	inversion = int(request.GET.get('inversion', False))
	eqid = (formulaID, inversion)

	for i in [one, two]:
		if i != 'empty':
			values.append(int(i))

	
	if values:
		result = calcVal(eqid,values)
	
	else:
		result = ''	

	return render(request, "index.html", {'eqlist':eqlist, 'invlist':invlist, 'context':context, 'values':values, 'result':result, 'one':eqid}) 





def calcVal(eqid, values):
	
	if eqid == (1,1):   # Force = Mass*Acceleration
		m = values[0]
		a = values[1]

		result = m*a
		return result

	if eqid == (1,2): # Mass = Force/Acceleration
		F = values[0]
		a = values[1]

		result = F/a
		return result

	if eqid == (1,3): #Acceleration = Force/Mass
		F = values[0]
		m = values[1]

		result = F/m
		return result

	if eqid == (2,1): #Momentum = Mass*Velocity
		m = values[0]
		v = values[1]

		result = m*v
		return result

	if eqid == (2,2): #Mass = Momentum/Velocity
		p = values[0]
		v = values[1]

		result = p/v
		return result

	if eqid == (2,3): #Velocity = Momentum/Mass
		p = values[0]
		m = values[1]

		result = p/m
		return result



def base(request):
	
	equations = Equation.objects.all()


	return {'equations': equations}
