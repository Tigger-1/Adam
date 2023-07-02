from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmpApp.serializers import EmployeeSerializer
from EmpApp.serializers import BranchSerializer
from EmpApp.models import Employee
from EmpApp.models import Branch

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employee = Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(employee_id=id)
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employee.objects.get(employee_id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def branchApi(request,id=0):
    if request.method=='GET':
        branch = Branch.objects.all()
        branch_serializer=BranchSerializer(branch,many=True)
        return JsonResponse(branch_serializer.data,safe=False)
    elif request.method=='POST':
        branch_data=JSONParser().parse(request)
        branch_serializer=BranchSerializer(data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        branch_data=JSONParser().parse(request)
        branch=Branch.objects.get(branch_id=id)
        branch_serializer=BranchSerializer(branch,data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        branch=Branch.objects.get(branch_id=id)
        branch.delete()
        return JsonResponse("Deleted Successfully",safe=False)
