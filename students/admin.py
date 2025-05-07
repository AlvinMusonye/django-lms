from django.contrib import admin
from .models import Student, Course , Enrollment

admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Course)


# Register your models here.
