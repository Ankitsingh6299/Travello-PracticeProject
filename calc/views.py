from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    mydict={
        'name':'Ankit Singh'
    }
    return render(request,'home.html',context=mydict)
def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])
    result=a+b
    dicti={
        "result":result
    }
    return render(request,'result.html',context=dicti)