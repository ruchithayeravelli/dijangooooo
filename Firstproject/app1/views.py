from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# from django.shortcuts import render 
# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("hello world,i am from view1")
def view2(request):
    return HttpResponse("hello world,i am from view2")
def view4(request):
    return JsonResponse({"name":"Ruchitha","message":"hello world"})
def dynamicview(request):
    gp1=request.GET.get("name") #getting query param from
    return HttpResponse(f"hello {gp1}")
def personInfo(request):
    name=request.GET.get("name","harish")
    city=request.GET.get("city","hyd")
    role=request.GET.get("role","Software")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})
def temp1(request):
    return render(request, "simple.html")
