from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
from .models import Interests_Model

# Create your forms here.
class Interests_Form(forms.ModelForm):

    class Meta:
        model = Interests_Model
        fields = "__all__"

    # qualification = forms.CharField(widget=forms.Textarea())
    # emp_stat = forms.CharField(widget=forms.Textarea())
    # skill = forms.CharField(widget=forms.Textarea())
    # hobbies = forms.CharField(widget=forms.Textarea())
    # courses = forms.CharField(widget=forms.Textarea())
    # extracurricular = forms.CharField(widget=forms.Textarea())
    # achievements = forms.CharField(widget=forms.Textarea())
    # passion = forms.IntegerField()
    # salary = forms.IntegerField()
    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


# from django import forms  
class StudentForm(forms.Form):   
    file= forms.FileField() # for creating file input  