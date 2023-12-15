from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('admissions',views.admissions,name='admissions'),
    path('jobsav',views.jobsav,name='jobsav'),
]