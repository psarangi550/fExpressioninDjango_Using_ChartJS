import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","fExpressionProject.settings")

import django

django.setup()

from faker import Faker

import random

from fExpressionApp.models import Employee

fake=Faker("en-IN")

def populate(n):
    for i in range(n):
        eno=random.randint(0000,9999)
        ename=fake.name()
        esal=random.randint(00000,99999)
        eaddr=fake.address()
        Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)

populate(25)
