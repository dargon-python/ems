import os
import uuid

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from emsapp.models import Emplist
# Create your views here.

def emplist(request):
    # status = request.session.get("status")
    # if status == 'ok':
    emp = Emplist.objects.all()
    pgnumber = request.GET.get("pgnumber")
    if pgnumber:
        pass
    else:
        pgnumber = 1
    page = Paginator(emp,per_page=3).page(pgnumber)

    return render(request,"emsapp/emplist.html",{"page":page})
    # return redirect("login_regist_app:login")

def addemp(request):
    # status = request.session.get("status")
    # if status == 'ok':
    return render(request,"emsapp/addEmp.html")
    # return redirect("login_regist_app:login")

def addemplogic(request):
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    age = request.POST.get("age")
    headpic = request.FILES.get('headpic')  #注意是FILES获取
    ex = os.path.splitext(headpic.name)
    headpic.name = str(uuid.uuid4())+ex[1]
    result = Emplist.objects.filter(name=name)
    if result:
        return HttpResponse("该员工已存在,添加失败")
    Emplist.objects.create(name=name,salary=salary,age=age,headpic=headpic)
    page = Paginator(Emplist.objects.all(),per_page=3)
    # page = page.page(page.num_pages)
    pgnumber = page.num_pages
    url = reverse('emsapp:emplist') + '?pgnumber=' + str(pgnumber)
    return redirect(url)

def deleteemp(request):
    pgnumber = int(request.GET.get("pgnumber"))
    id = request.GET.get('id')
    emp = Emplist.objects.filter(id=id)[0]
    emp.delete()
    page = Paginator(Emplist.objects.all(),per_page=3)
    if pgnumber >= page.num_pages:
        page = page.page(page.num_pages)
    else:
        page = page.page(pgnumber)
    url = reverse('emsapp:emplist')+'?pgnumber='+str(page.number)
    return redirect(url)

def updataemp(request):
    # status = request.session.get("status")
    # if status == 'ok':
    pgnumber = request.GET.get("pgnumber")
    id = request.GET.get('id')
    emp = Emplist.objects.filter(id=id)[0]
    name = emp.name
    salary = emp.salary
    age = emp.age
    return render(request,"emsapp/updateEmp.html",{"id":id,"name":name,"salary":salary,"age":age,"pgnumber":pgnumber})
    # return redirect("login_regist_app:login")

def updataemplogic(request):
    pgnumber = int(request.GET.get("pgnumber"))
    print(pgnumber)
    id = request.GET.get('id')
    print(id)
    emp = Emplist.objects.filter(id=id)[0]
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    age = request.POST.get("age")
    headpic = request.FILES.get('headpic')
    emp.name = name
    emp.salary = salary
    emp.age = age
    emp.headpic = headpic
    emp.save()
    # page = Paginator(Emplist.objects.all(), per_page=3).page(pgnumber)
    # return render(request, "emsapp/emplist.html", {"page": page})
    url = reverse('emsapp:emplist')+'?pgnumber='+str(pgnumber)
    return redirect(url)

