from rest_framework import serializers
from employees.models import Employee, EmployeeTask

        
class EmployeeTaskSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),many=False)
    class Meta:
        model = EmployeeTask
        fields = ('pk','task_name','employee','task_desc','created_date','deadline')


class EmployeeSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    # tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tasks = EmployeeTaskSerializer(read_only=True,many=True)
    class Meta:
        model = Employee
        # fields = ('pk','emp_id','name','gender','designation','tasks')
        fields='__all__'