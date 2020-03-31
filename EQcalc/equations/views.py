from django.shortcuts import render


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
	three = request.GET.get('3', 'empty')
	four = request.GET.get('4', 'empty')
	five = request.GET.get('5', 'empty')
	six = request.GET.get('6', 'empty')
	seven = request.GET.get('7', 'empty')
	eight = request.GET.get('8', 'empty')
	nine = request.GET.get('9', 'empty')


	formulaID = int(request.GET.get('formulaID', False))
	inversion = int(request.GET.get('inversion', False))
	eqid = (formulaID, inversion)

	for i in [one, two, three, four, five, six, seven, eight, nine]:
		if i != 'empty':
			values.append(int(i))

	
	if values:
		result = calcVal(eqid,values)
	
	else:
		result = ''	
	# if invlist:

	# 	test = invlist[0].inputs.all()
	# else:
	# 	test=''

	return render(request, "index.html", {'eqlist':eqlist, 'invlist':invlist, 'context':context, 'values':values, 'result':result, 'one':eqid,}) #'test':test}) 





def calcVal(eqid, values):
	
	if eqid == (1,1):   # Force = Mass*Acceleration
		a = values[0]
		m = values[1]

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
		v = values[0]
		m = values[1]

		result = m*v
		return result

	if eqid == (2,2): #Mass = Momentum/Velocity
		v = values[0]
		p = values[1]

		result = p/v
		return result

	if eqid == (2,3): #Velocity = Momentum/Mass
		p = values[0]
		m = values[1]

		result = p/m
		return result

	if eqid == (3,1): #Final_Position=Initial_Position+Velocity*Time+0.5*Acceleration*Time^2
		v = values[0]
		a = values[1]
		xi = values[2]
		t = values[3]
		

		result = xi+(v*t)+0.5*a*t**2
		return result


	if eqid == (3,2): #Initial_Position=Final_Position-Velocity*Time-0.5*Acceleration*Time^2
		v = values[0]
		a = values[1]
		xf = values[2]
		t = values[3]
		

		result = xf-(v*t)-0.5*a*t**2
		return result

	if eqid == (3,3): #Velocity=(FinalPosition-InitialPosition-0.5*Time^2)/Time
		a = values[0]
		xi = values[1]
		xf = values[2]
		t = values[3]
		

		result = (xf-xi-0.5*a*t**2)/t
		return result


	if eqid == (3,4): #Acceleration=(FinalPosition-InitialPosition-Velocity*Time)/(0.5*Time^2)
		v = values[0]
		xi = values[1]
		xf = values[2]
		t = values[3]
		

		result = (xf-xi-v*t)/(0.5*t**2)
		return result


	if eqid == (3,5): #Time=QuadraticFormula
		v = values[0]
		a = values[1]
		xi = values[2]
		xf = values[3]
		

		result = ((-v+(v**2-2*a*(xi-xf))**0.5)/a, (-v-(v**2-2*a*(xi-xf))**0.5)/a)
		return result	









def base(request):
	
	equations = Equation.objects.all()


	return {'equations': equations}
