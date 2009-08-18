from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    established_on = models.DateField()
    
    def __unicode__(self):
        return self.dept_name
    
class Level(models.Model):
    level_name = models.CharField(max_length = 100)
    pay_min = models.PositiveIntegerField()
    pay_max = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.level_name
    
class Employee(models.Model):
    emp_name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department)
    level = models.ForeignKey(Level)
    reports_to = models.ForeignKey('self', null=True, blank=True)
    
    pay = models.PositiveIntegerField()
    joined_on = models.DateField()
    
class Leave(models.Model):
    employee = models.ForeignKey(Employee)
    leave_day = models.DateField()
    
    
"""
import random
from datetime import timedelta, date
import pickle
names = pickle.load(file('/home/shabda/names.pickle'))
for i in range(1000):
    emp = Employee()
    emp.name = random.choice(names)
    emp.department = random.choice(list(Department.objects.all()))
    emp.level = random.choice(Level.objects.all())
    try: emp.reports_to = random.choice(list(Employee.objects.filter(department=emp.department)))
    except:pass
    emp.pay = random.randint(emp.level.pay_min, emp.level.pay_max)
    emp.joined_on = emp.department.established_on + timedelta(days = random.randint(0, 200))
    emp.save()
"""

"""
employees = list(Employees.objects.all())
for i in range(100):
    employee = random.choice(employees)
    leave = Leave(employee = employee)
    leave.leave_day = date.today() - timedelta(days = random.randint(0, 365))
    leave.save()
    
"""
