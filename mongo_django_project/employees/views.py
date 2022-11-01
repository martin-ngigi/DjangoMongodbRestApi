from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from employees.models import Employee, EmployeeTask
from employees.serializers import EmployeeSerializer, EmployeeTaskSerializer


@csrf_exempt
def employee_list(request):
	if request.method == 'GET':
		emp = Employee.objects.all()
		emp_serializer = EmployeeSerializer(emp, many=True)
		return JsonResponse(emp_serializer.data, safe=False)

	elif request.method == 'POST':
		emp_data = JSONParser().parse(request)
		emp_serializer = EmployeeSerializer(data=emp_data)
		
		if emp_serializer.is_valid():
			emp_serializer.save()
			return JsonResponse(emp_serializer.data,status=201)
		return JsonResponse(emp_serializer.errors,status=400)

@csrf_exempt
def employee_detail(request, pk):
	try:
		emp = Employee.objects.get(pk=pk)
	except Employee.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		emp_serializer = EmployeeSerializer(emp)
		return JsonResponse(emp_serializer.data)
	elif request.method == 'DELETE':
		emp.delete()
		return HttpResponse(status=204)


@csrf_exempt
def employeetask_list(request):
	if request.method == 'GET':
		emptask = EmployeeTask.objects.all()
		emptask_serializer = EmployeeTaskSerializer(emptask, many=True)
		return JsonResponse(emptask_serializer.data, safe=False)
	elif request.method == 'POST':
		emptask_data = JSONParser().parse(request)
		emptask_serializer = EmployeeTaskSerializer(data=emptask_data)
		if emptask_serializer.is_valid():
			emptask_serializer.save()
			return JsonResponse(emptask_serializer.data,status=201)
		return JsonResponse(emptask_serializer.errors,status=400)

@csrf_exempt
def employeetask_detail(request, pk):
	try:
		emptask = EmployeeTask.objects.get(pk=pk)
	except EmployeeTask.DoesNotExist:
		return HTTPResponse(status=404)

	if request.method == 'GET':
		emptask_serializer = EmployeeTaskSerializer(emptask)
		return JsonResponse(emptask_serializer.data)
	
	elif request.method == 'DELETE':
		emptask.delete()
		return HttpResponse(status=204)
