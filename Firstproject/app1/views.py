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
students =[
    {
        "id": 1,
        "name": "Ruchitha",
        "age": 21,
        "course": "B.Pharmacy",
        "city":"hyd",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Kavya",
        "age": 22,
        "course": "B.Pharmacy",
        "city":"hyd",
        "marks": 78
    },
    {
        "id": 3,
        "name": "Anjali",
        "age": 20,
        "course": "B.Sc",
        "city":"kerala",
        "marks": 90
    }
]
def studentsBycity(request,city):
    filterData=[]
    for student in students:
        if student["city"].lower()==city.lower():
            filterData.append(student)
    if len(filterData)>0:
      return JsonResponse({"data":filterData,"message":"students records successfully feched"},status=200)
    elif len(filterData)==0:
        return JsonResponse({"data":filterData,"message":"no content available"})
    else:
        return JsonResponse({"error":"something"})
def studentsBymarks(request,marks):
    filterData=[]
    for student in students:
        if student["marks"]>marks:
            filterData.append(student)
    if len(filterData)>0:
      return JsonResponse({"data":filterData,"message":"students records successfully feched"},status=200)
    elif len(filterData)==0:
        return JsonResponse({"data":filterData,"message":"no content available"})
    else:
        return JsonResponse({"error":"something"})
    # Task
    # ecomers data
    # create api to fetch product details 
    # a.by category by string formate
    # b.by rating  by float formate
