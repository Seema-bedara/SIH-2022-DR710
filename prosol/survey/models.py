from pyexpat import model
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Interests_Model(models.Model):

    qualification = models.TextField()
    emp_stat = models.TextField()
    skill = models.TextField()
    hobbies = models.TextField()
    courses = models.TextField()
    extracurricular = models.TextField()
    achievements = models.TextField()
    passion = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.title


class Post(models.Model):
    PDF = models.FileField(null=True, 
                           blank=True, 
                           validators=[FileExtensionValidator( ['pdf'] ) ])

class Jobs(models.Model):
    job = models.CharField(max_length = 100)
    intermediate = models.CharField(max_length = 100)
    bachelors = models.CharField(max_length = 100)


# # from django.db import models
# class TestModel(models.Model):
    
#     def pdf_upload_path(instance, filename):
#         return f'utility_bills/{instance.created_date.strftime("%Y-%m-%d")}_test_{filename}'

#     created_date = models.DateTimeField(
#         auto_now=False, 
#         auto_now_add=True, 
#         null=True, 
#         blank=True, 
#     )
#     pdf = models.FileField(upload_to=pdf_upload_path, blank=True)

class pdftxt(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.title