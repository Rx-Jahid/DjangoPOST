from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def add(request):
    
    coll1= request.POST['rx1']
    coll2= request.POST['rx2']
    cl=coll1+coll2
    return render(request,'home/add.html',{'col':coll1})


