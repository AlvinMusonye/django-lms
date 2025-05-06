from django.urls import path
from .views import index, students_list, courses, app, blogs
urlpatterns = [
     path('', index, name='index'),
     path('students/',students_list, name='students'),
     path('courses/',courses, name='courses'),
     path('app/',app, name='app'),
     path('blogs/',blogs, name ='blogs'),

     
]