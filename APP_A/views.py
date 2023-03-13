from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'ms_dhoni','age':34,'stream':'all rounder'}
    return render(request,'jinja_print.html',context=d)