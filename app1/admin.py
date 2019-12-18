from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','addr']

#admin.site.register(Student)
admin.site.register(Student,StudentAdmin)
