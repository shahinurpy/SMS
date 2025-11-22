from django.db import models
from django.conf import settings

    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name
    
class Subject(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="subject")
    subject_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name
    
