from django.db import models

# Create your models here.

# Link https://www.geeksforgeeks.org/serializer-relations-django-rest-framework/

GENDER_CHOICES = (('M','Male'),
					('F','Female'),)

class Employee(models.Model):
	emp_id = models.IntegerField()
	name = models.CharField(max_length=150)
	gender = models.CharField(max_length=1,
							choices=GENDER_CHOICES,
							default='M')
	designation = models.CharField(max_length=150)

	class Meta:
		ordering=('emp_id',)

	def __str__(self):
		return self.name

#  The EmployeeTask model holds a ManyToOne relationship with the Employee model
# The same task will not be assigned to more than one employee, but one employee can have multiple tasks.
# Hence, the EmployeeTaskSerializer class should serialize only a single employee instance, whereas, EmployeeSerializer class should serialize one or more EmployeeTask instances (more than one task can be assigned to an employee). 
class EmployeeTask(models.Model):
	task_name = models.CharField(max_length=150)
	employee = models.ForeignKey(Employee,
								related_name='tasks',
								on_delete=models.CASCADE)
	task_desc = models.CharField(max_length=350)
	created_date = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()

	class Meta:
		ordering = ('task_name',)

	def __str__(self):
		return self.task_name
