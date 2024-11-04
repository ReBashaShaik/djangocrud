import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbvproject.settings')

import django

django.setup()

from crudapp.models import *

from faker import Faker

from random import *

faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        feaddr=faker.city()
        emp_record=employee.objects.get_or_create(eno=feno, ename=fename,esal=fesal, eaddr=feaddr)
populate(20)


# the above code is used to generate fake data
# After writing code
# we have to run two commands in cmd
# 1) pip install faker
# 2) python populate.py  ( we must run this command to push data into table).