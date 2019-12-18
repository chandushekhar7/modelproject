from django.shortcuts import render
from .models import Student
# Create your views here.

def studentinfo(request):
    stu = Student.objects.all()
    print(stu)
    return render(request,'app1/home.html',{'stu':stu})
