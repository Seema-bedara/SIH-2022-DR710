from django.urls import path
from . import views

urlpatterns = [
    path('',views.survey, name = 'survey'),
    path('result',views.result,name='result'),
    path('upload',views.upload,name='upload'),
    #path('resultCV',views.resultCV,name='resultCV')
]