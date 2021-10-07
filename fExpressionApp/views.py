from django.shortcuts import render,HttpResponse
from django.db.models import F #importing the F Objects
from .models import Employee

# Create your views here.

def index_view(request):
    emps=Employee.objects.all()
    # emps=Employee.objects.all().update(eno=F("eno")+1)
    return render(request, "fExpressionApp/index.html", {"emps":emps})
    # return HttpResponse("")
