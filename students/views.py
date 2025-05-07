from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
 
    ctx = {'name': 'Alvin Doe'}
    return render(request, 'index.html', ctx)

def students_list(request):
    students = [
        {'first_name' : 'John', 'last_name' : 'Doe', 'email' : 'johndoe@gmail.com'},
        {'first_name' : 'Jane', 'last_name' : 'Smith', 'email' : 'janeSmith@gmail.com'},
        {'first_name' : 'Bob', 'last_name' : 'Joe', 'email' : 'Bobjoe@gmail.com'}
    ]
    ctx = {'students': students}
    return render(request, 'students_list.html', ctx)

def students_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students_list.html', ctx  )

def courses(request):
    course =[
        {'course_name' : 'software Engineering, '},
        { 'course_name' : 'Devops'},
        {'course_name' :'Data Science'}

    ]
    ctx = {'course' : course}
    return render(request, 'course.html', ctx)


def app(request):
    App =[
        {'Welcome to my App '},
       

    ]
    ctx = {'app' : app}
    return render(request, 'App.html', ctx)

def blogs(request):
    Blogs = [
        {'title' : 'Learning Django', 'content' :'Django is an Awesome open source framework for building APIs using Django REST framework','author' : 'John Doe' , 'date' : '2025-5-5' }
    ]
    ctx = {'blogs' : blogs}
    return render(request, 'blog_list.html', ctx)



def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

