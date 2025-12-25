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
products = [
    {
        "id": "P101",
        "name": "Wireless Earbuds",
        "category": "Electronics",
        "brand": "Boat",
        "price": 2499,
        "stock": 120,
        "rating": 4.3,
        "city": "Hyderabad"
    },
    {
        "id": "P102",
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "brand": "JBL",
        "price": 3499,
        "stock": 60,
        "rating": 4.6,
        "city": "Bengaluru"
    },
    {
        "id": "P103",
        "name": "Cotton T-Shirt",
        "category": "Fashion",
        "brand": "HRX",
        "price": 799,
        "stock": 200,
        "rating": 4.1,
        "city": "Mumbai"
    },
    {
        "id": "P104",
        "name": "Sports Shoes",
        "category": "Footwear",
        "brand": "Nike",
        "price": 4999,
        "stock": 85,
        "rating": 4.7,
        "city": "Delhi"
    },
    {
        "id": "P105",
        "name": "Smart Watch",
        "category": "Electronics",
        "brand": "Noise",
        "price": 2999,
        "stock": 150,
        "rating": 4.4,
        "city": "Pune"
    }
]

from django.http import JsonResponse

def productByRating(request, rating):
    try:
        converted_rating = float(rating)

        if request.method == "GET":
            filterData = []

            for product in products:   # make sure products is defined
                if product['rating'] <= converted_rating:
                    filterData.append(product)

            msg = "No products found" if not filterData else "Products fetched successfully"

            return JsonResponse({
                "status": "Success",
                "data": filterData,
                "msg": msg
            })

        return JsonResponse({"status": "failure", "message": "Only GET method allowed"})

    except Exception as e:
        return JsonResponse({"status": "failure", "message": str(e)})
