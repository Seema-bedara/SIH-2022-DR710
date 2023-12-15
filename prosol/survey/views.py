from logging.config import dictConfig
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse,redirect
from .forms import Interests_Form, PostForm
from .models import Interests_Model, Jobs
from .sih import gimme_result
import pandas as pd
import PyPDF2
import os


# Create your views here.
dict_req = {}
def survey(request):
    if request.method == 'POST':
        context = ""
        
        # context += (request.POST['qualification'])
        # context += " "
        context += (request.POST['emp_stat'])
        context += " "
        context += (request.POST['skill'])
        context += " "
        context += (request.POST['hobbies'])
        context += " "
        context += (request.POST['courses'])
        context += " "
        context += (request.POST['extracurricular'])
        context += " "
        context += (request.POST['achievements'])
        context += " "
        passion = int(request.POST['passion'])
        salary = int(request.POST['salary'])
        pas = passion/salary
        
        res_dict={"context":context, "passion":passion, "salary":salary}
        dict_req = res_dict
        liststr = list(context)
        for i in range(0, len(liststr)):
            if liststr[i] == '\n':
                liststr[i] = ' '

        result,prob = gimme_result(context)
        list_prob = prob[0]
        proba = {}
        for i in range(0, len(list_prob)):
            proba[i] = list_prob[i]
        proba = {k: v for k, v in sorted(proba.items(), key=lambda item: item[1])}
        lkey = list(proba.keys())
        p1 = proba[lkey[-1]]
        p2 = proba[lkey[-2]]
        p3 = proba[lkey[-3]]
        dict_job = {32: 'HR',
            22: 'DESIGNER',
            44: 'SDE',
            45: 'TEACHER',
            2: 'ADVOCATE',
            15: 'BUSINESS-DEVELOPMENT',
            31: 'HEALTHCARE',
            30: 'FITNESS',
            3: 'AGRICULTURE',
            12: 'BPO',
            14: 'BUSINESS ANALYST AND SALES AND SALES',
            19: 'CONSULTANT',
            23: 'DIGITAL-MEDIA',
            6: 'AUTOMOBILE',
            16: 'CHEF',
            29: 'FINANCE',
            4: 'APPAREL',
            36: 'MECHANICAL ENGINEERING',
            0: ' SDE',
            17: 'CIVIL ENGINEERING',
            26: 'ELECTRICAL ENGINEERING',
            10: 'BIO MEDICAL ENGINEERING',
            28: 'ENVIRONMENTAL ENGINEERING',
            41: 'PRODUCT MANAGER',
            40: 'PRODUCCT MANAGER',
            27: 'ENGINEERING',
            1: 'ACCOUNTANT',
            18: 'CONSTRUCTION',
            42: 'PUBLIC-RELATIONS',
            9: 'BANKING',
            5: 'ARTS',
            7: 'AVIATION',
            21: 'DATA SCIENCE',
            8: 'Arts',
            46: 'WEB DEVELOPER',
            35: 'MECHANICAL ENGINEER',
            33: 'Health and fitness',
            20: 'Civil Engineer',
            34: 'Java Developer',
            13: 'BUSINESS ANALYST AND SALES',
            38: 'Operations Manager',
            43: 'Python Developer',
            25: 'DevOps Engineer',
            37: 'NETWORK SECURITY ENGINEER',
            39: 'PMO',
            24: 'Database',
            11: 'BLOCKCHAIN'}
        # print(proba)
        # a = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-1]][0][0]
        # b = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-2]][0][0]
        # c = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-3]][0][0]
        b = dict_job[lkey[-2]]
        c = dict_job[lkey[-3]]

        # my_data = Jobs.objects.all()
        # from mysqlx import Row
        # import psycopg2

        # DB_NAME = "SIH"
        # DB_USER = "postgres"
        # DB_PASS = "SQL123"
        # DB_HOST = "localhost:8000"
        # DB_PORT = "5432"
        # conn = psycopg2.connect(database=DB_NAME,
        # 						user=DB_USER,
        # 						password=DB_PASS,
        # 						host=DB_HOST,
        # 						port=DB_PORT)
        # # print("Database connected successfully")

        # cur = conn.cursor()
        # cur.execute("SELECT * FROM survey_jobs")
        # rows = cur.fetchall()
        # for data in rows:
        # 	# print("ID :" + str(data[0]))
        # 	# print("NAME :" + data[1])
        # 	# print("EMAIL :" + data[2])
        #     if data[1] == result:
        #         dat1 = list(data[2],data[3])
        #     elif data[1] == b:
        #         dat2 = list(data[2],data[3])
        #     elif data[1] == c:
        #         dat3 =  list(data[2],data[3])
        # # print('Data fetched successfully')
        # conn.close()

        result =result + "    ("+ str(round(p1*100,2)) + " %)"
        b = b + "    (" + str(round(p2*100,2)) + " %)"
        c = c + "    (" + str(round(p3*100,2)) + " %)"
        res = {'context':result,'b':b,'c':c}
        return render(request ,"result.html", res)
    
    # else:
    #     form = PostForm()
    #     return render(request,"result.html",{"form":form})

    # context ={}

    # form = Interests_Form(request.POST or None, request.FILES or None)

    # if form.is_valid():
    #     form.save()

    # context['form']= form
    else:
        return render(request , 'survey.html')

def result(request):         

    # conn = psycopg2.connect(
    # database="SIH", user='postgres', password='SQL123', host='127.0.0.1', port= '5432')
    
    # conn.autocommit = True
    # cursor = conn.cursor()
    # cursor.execute('''SELECT * from survey_interests_model''')
    # # a,b = Interests_Model.objects.get("skill")
    # res = cursor.fetchone()
    # res = list(res)
    # result = ""
    # for i in res:
    #     result += i + " "
    result = gimme_result("python")
    # context = {'result':result} 
    return render(request,'result.html')   


    # from django.shortcuts import render  
# from django.http import HttpResponse  
# from survey.functions.functions import handle_uploaded_file  
# from survey.forms import StudentForm  
# def index(request):  
#     if request.method == 'POST':  
#         student = StudentForm(request.POST, request.FILES)  
#         if student.is_valid():  
#             handle_uploaded_file(request.FILES['file'])  
#             return HttpResponse("File uploaded successfuly")  
#     else:  
#         student = StudentForm()  
#         return render(request,"survey.html",{'form':student})  

def upload(request):
    if request.method == 'POST':
        # handle_uploaded_file(request.FILES['file'])
        filepdf = request.FILES['file']
        from PyPDF2 import PdfReader
        reader = PdfReader(filepdf)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        liststr = list(text)
        for i in range(0, len(liststr)):
            if liststr[i] == '\n':
                liststr[i] = ' '
        data2 = ''.join(liststr)
        data2 = str(data2)
        result,prob = gimme_result(data2)
        list_prob = prob[0]
        proba = {}
        for i in range(0, len(list_prob)):
            proba[i] = list_prob[i]
        proba = {k: v for k, v in sorted(proba.items(), key=lambda item: item[1])}
        lkey = list(proba.keys())
        p1 = proba[lkey[-1]]
        p2 = proba[lkey[-2]]
        p3 = proba[lkey[-3]]
        dict_job = {32: 'HR',
            22: 'DESIGNER',
            44: 'SDE',
            45: 'TEACHER',
            2: 'ADVOCATE',
            15: 'BUSINESS-DEVELOPMENT',
            31: 'HEALTHCARE',
            30: 'FITNESS',
            3: 'AGRICULTURE',
            12: 'BPO',
            14: 'BUSINESS ANALYST AND SALES AND SALES',
            19: 'CONSULTANT',
            23: 'DIGITAL-MEDIA',
            6: 'AUTOMOBILE',
            16: 'CHEF',
            29: 'FINANCE',
            4: 'APPAREL',
            36: 'MECHANICAL ENGINEERING',
            0: ' SDE',
            17: 'CIVIL ENGINEERING',
            26: 'ELECTRICAL ENGINEERING',
            10: 'BIO MEDICAL ENGINEERING',
            28: 'ENVIRONMENTAL ENGINEERING',
            41: 'PRODUCT MANAGER',
            40: 'PRODUCCT MANAGER',
            27: 'ENGINEERING',
            1: 'ACCOUNTANT',
            18: 'CONSTRUCTION',
            42: 'PUBLIC-RELATIONS',
            9: 'BANKING',
            5: 'ARTS',
            7: 'AVIATION',
            21: 'DATA SCIENCE',
            8: 'Arts',
            46: 'WEB DEVELOPER',
            35: 'MECHANICAL ENGINEER',
            33: 'Health and fitness',
            20: 'Civil Engineer',
            34: 'Java Developer',
            13: 'BUSINESS ANALYST AND SALES',
            38: 'Operations Manager',
            43: 'Python Developer',
            25: 'DevOps Engineer',
            37: 'NETWORK SECURITY ENGINEER',
            39: 'PMO',
            24: 'Database',
            11: 'BLOCKCHAIN'}
        # print(proba)
        # a = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-1]][0][0]
        # b = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-2]][0][0]
        # c = [new_k for new_k in dict_job.items() if new_k[1] == lkey[-3]][0][0]
        b = dict_job[lkey[-2]]
        c = dict_job[lkey[-3]]
        result =result + "    ("+ str(round(p1*100,2)) + " %)"
        b = b + "    (" + str(round(p2*100,2)) + " %)"
        c = c + "    (" + str(round(p3*100,2)) + " %)"

        res = {'context':result,'b':b,'c':c}
        return render(request ,"result.html", res)