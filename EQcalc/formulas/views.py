from django.shortcuts import render
from variables.models import Variable
from formulas.models import Formula

# Create your views here.



def index(request):
	
	return render(request, "index.html") 

def first(request):

	form = request.POST.get('var', False)
	inputbox =[]
	resultout = ''
	refout = ''
	visual = ''

	if form == 'vf':
		inputbox = ['Initial Velocity', 'Acceleration', 'Time']
		visual = 'vf = vi + a*t'
		refout = 'vf'

	elif form == 'vi':
		inputbox = ['Final Velocity', 'Acceleration', 'Time']
		visual = 'vi = vf - a*t'
		refout = 'vi'

	elif form == 'a':
		inputbox = ['Final Velocity', 'Inital Velocity', 'Time']
		visual = 'a = (vf - vi)/t'
		refout = 'a'

	elif form == 't':
		inputbox = ['Final Velocity', 'Inital Velocity', 'Acceleration']
		visual = 't = (vf - vi)/a'
		refout = 't'	


	value1 = request.POST.get('val1', False)
	value2 = request.POST.get('val2', False)
	value3 = request.POST.get('val3', False)
	vals = [value1, value2, value3]
	if request.POST.get('refin', False) == 'vf':
		inputbox = ['Initial Velocity', 'Acceleration', 'Time']
		visual = 'vf = vi + a*t'
		vi = int(value1)
		a = int(value2)
		t = int(value3)
		result = vi + a*t 
		resultName = 'Final Velocity= '
		resultout = [resultName, result]
		refout = 'vf'

	elif request.POST.get('refin', False) == 'vi':
		inputbox = ['Final Velocity', 'Acceleration', 'Time']
		visual = 'vi = vf - a*t'
		vf = int(value1)
		a = int(value2)
		t = int(value3)
		result = vf - a*t 
		resultName = 'Final Velocity= '
		resultout = [resultName, result]
		refout = 'vi'

	elif request.POST.get('refin', False) == 'a':
		inputbox = ['Final Velocity', 'Inital Velocity', 'Time']
		visual = 'a = (vf - vi)/t'
		vf = int(value1)
		vi = int(value2)
		t = int(value3)
		result = (vf - vi)/t
		resultName = 'Acceleration= '
		resultout = [resultName, result]
		refout = 'a'

	elif request.POST.get('refin', False) == 't':
		inputbox = ['Final Velocity', 'Inital Velocity', 'Acceleration']
		visual = 't = (vf - vi)/a'
		vf = int(value1)
		vi = int(value2)
		a = int(value3)
		result = (vf - vi)/a
		resultName = 'Time = '
		resultout = [resultName, result]
		refout = 't'


	return render(request, "first.html", {

		"num":form, 
		'inputbox':inputbox, 
		'vals':vals, 
		'refout':refout, 
		'resultout':resultout,
		'visual':visual
		})




def first_db(request):

	formulas = Formula.objects.all()
	Acceleration = 5
	Mass = 10
	result = Formula.objects.all().get(name = 'F=ma').express1
	result = eval(result)
	

	return render(request, "first_db.html", {"formulas":formulas, 'result':result})
# if($_POST['']){
	

# }


def equationPage(request):
	
	equations = Formula.objects.all()
	
		

	return render(request, 'equationPage.html', {'equations':equations})


def formPage(request):

	name = request.POST['equation']
	equation = Formula.objects.get(name = name)
	
	paramList = [
		equation.param1,
		equation.param2,
		equation.param3,
		equation.param4
	]

	expressList = [
		equation.express1,
		equation.express2,
		equation.express3,
		equation.express4
	]


	formlist = []
	

	for x,y in zip(paramList, expressList):
		if x != '' and y != '':
			formlist.append([x,y])

	
	equation = equation.param4

	return render(request, 'formPage.html', {'equation':equation, 'formlist':formlist})



def calcPage(request):
	
	
	form = request.GET.get('form', False)

	paramList = []
	param = ''
	endList = [' ', '*', '+', '-', '/', '**', '(', ')'] 
	if type(form) != bool:
		for i in range(len(form)):
			if form[i] not in endList and i != len(form)-1:
				param = param + form[i]
			
			elif param != '' and i == len(form)-1:
				param = param + form[i]
				paramList.append(param)
				param = ''

			elif param != '':
				paramList.append(param)
				param = ''
	

	one = int(request.POST.get('1', False))
	two = int(request.POST.get('2', False))	
	three = int(request.POST.get('3', False))

	if (request.POST.get('1', False)) != False:
		one = int(request.POST.get('1', False))
	else:
		one = 1

	if (request.POST.get('2', False)) != False:
		two = int(request.POST.get('2', False))
	else:
		two = 1

	if (request.POST.get('3', False)) != False:
		three = int(request.POST.get('3', False))
	else:
		three = 1



	# paramList.append(one)
	out = [paramList, form]
	numbers = ['one', 'two', 'three', 'four']
	newForm = ''

	newForm = form
	for param, num in zip(paramList,numbers):
		newForm = newForm.replace(param, num)


	result = eval(newForm)



	return render(request, 'calcPage.html', {'paramList':paramList,
	 										'one':[one,two,three],
	 										 'out':out,
	   										'newForm':newForm, 
	   										'result':result})

















