from django.shortcuts import render


from .models import Equation, Units

# Create your views here.

def index(request, **kwarg):


	context = kwarg
	if 'eq' in kwarg and 'inv' in kwarg: # formulaId and inversion coming in dyn Url
		eq = kwarg['eq'] # choosing both formID and inversion
		inv = kwarg['inv']
		eqlist = Equation.objects.filter(formulaID=eq)
		invlist = Equation.objects.filter(inversion=inv,formulaID=eq)
	elif 'eq' in kwarg and 'inv' not in kwarg: #if at first step of just choosing formID and not inversion
		eq = kwarg['eq']
		eqlist = Equation.objects.filter(formulaID=eq)
		invlist =[]
	else:
		eqlist = []
		invlist = []

	values = []
	one = request.GET.get('1', 'empty') #inputs vary in number depending on formula. ideally would be done in cleaner way
	two = request.GET.get('2', 'empty')
	three = request.GET.get('3', 'empty')
	four = request.GET.get('4', 'empty')
	five = request.GET.get('5', 'empty')
	six = request.GET.get('6', 'empty')
	seven = request.GET.get('7', 'empty')
	eight = request.GET.get('8', 'empty')
	nine = request.GET.get('9', 'empty')
	oneunit = request.GET.get('varUnit1', 'empty') #units for each variable inputed 
	twounit = request.GET.get('varUnit2', 'empty')
	threeunit = request.GET.get('varUnit3', 'empty')
	fourunit = request.GET.get('varUnit4', 'empty')
	fiveunit = request.GET.get('varUnit5', 'empty')
	sixunit = request.GET.get('varUnit6', 'empty')
	sevenunit = request.GET.get('varUnit7', 'empty')
	eightunit = request.GET.get('varUnit8', 'empty')
	nineunit = request.GET.get('varUnit9', 'empty')
	
	units = [oneunit, twounit, threeunit, fourunit, fiveunit, sixunit, sevenunit, eightunit, nineunit]
	inputvals = [one, two, three, four, five, six, seven, eight, nine]
	formulaID = int(request.GET.get('formulaID', False)) #from hidden formulaID GET request
	inversion = int(request.GET.get('inversion', False)) #from hidden inversion GET request
	eqid = (formulaID, inversion)
	


	for i in inputvals: #append list that then goes to calcVal functino to solve hardcoded eq
		if i != 'empty':
			values.append(int(i))
	
	if values: # call calcval funtion with correct formulaID and inversino and list of values
		result = calcVal(eqid,values)
	
	else:
		result = ''

	# values1 = [] # attaches inputs vars to units (just a test) to be used with preUnitConverter funtion
	# for i,j in zip(inputvals,units):
	# 	if i != 'empty':
	# 		values1.append((i,j))

	# valout = preUnitConverter(values1) 

	# if invlist:

	# 	test = invlist[0].inputs.all()
	# else:
	# 	test=''

	

	return render(request, "index.html", {'eqlist':eqlist,
										 'invlist':invlist, 
										 'context':context, 
										 'values':values, 
										 'result':result, 
										 'one':eqid,
										 'units':units,})
										 # 'values1':values1,
										 # 'valout':valout,}) #'test':test}) 



def preUnitConverter(valunit): 
	valuesout = []
	for pair in valunit:
		unit = Units.objects.get(name=pair[1]).unitConversion #finds correct unit based on input unit name.. 
		valuesout.append(int(pair[0])*unit) # and looks up unit conversion value associated with unit in DB,...
	return valuesout # then multiplies inputed value by that in order to convert to SI value



def postUnitConverter(val, numUnit, denUnit): # looks up unit conversion value for requested denominator and...
	num = Units.objects.get(name=numUnit).unitConversion #numerator of result variable. multiplies output values...
	den = Units.objects.get(name=denUnit).unitConversion #by den and divides it by num. output value comes from calcval function
	return (val*den/num)




def calcVal(eqid, values): # hardcoded formulas for each formula and inversion formula. ideally, input values directly associated with var, no just in list.
	
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
