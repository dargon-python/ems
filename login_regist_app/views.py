import random
import string

from django.shortcuts import render,HttpResponse,redirect

from login_regist_app.captcha.image import ImageCaptcha
from login_regist_app.models import User
# Create your views here.

def login(request):
    un = request.COOKIES.get("uname")
    up = request.COOKIES.get("upwd")
    status = request.session.get("status")
    addurl = request.GET.get("addurl")
    print(addurl,1)
    if (un and up) or status == 'ok':
        request.session["status"] = 'ok'
        return redirect("emsapp:emplist")
    return render(request,"login_regist_app/login.html",{"addurl":addurl})

def loginlogic(request):
    uname = request.POST.get("username")
    upwd = request.POST.get("userpwd")
    result = User.objects.filter(username=uname, password=upwd)
    if result.exists()==True:
        request.session["status"] = 'ok'
        addurl = request.POST.get("addurl")
        print(addurl,2)
        if addurl == 'addurl':
            return HttpResponse('addurl')
        remember = request.POST.get("remember")
        response = HttpResponse('ok')
        if remember:
            response.set_cookie("uname",uname,max_age=7*24*60*60)
            response.set_cookie("upwd",upwd,max_age=7*24*60*60)
        return response
    return HttpResponse('error')
    # return render(request,"emsapp/emplist.html")

def regist(request):
    return render(request,"login_regist_app/regist.html")

def registlogic(request):
    uname = request.POST.get("username")
    upwd1 = request.POST.get("userpwd1")
    upwd2 = request.POST.get("userpwd2")
    capt = request.POST.get("captcha")
    codes = request.session.get("codes")
    name = User.objects.filter(username=uname)
    # print(name,uname, upwd1, upwd2, capt.lower(), codes.lower())
    if name.exists()==False and upwd1==upwd2 and capt.lower() == codes.lower():
        User.objects.create(username=uname,password=upwd1)
        return  HttpResponse('ok')
    return HttpResponse('error')

def getcaptcha(request):
    image = ImageCaptcha()  # 声明一个图片验证码的对象
    # 生成一个随机码
    codes = random.sample(string.ascii_letters + string.digits, 5)
    codes = "".join(codes)
    request.session['codes'] = codes
    data = image.generate(codes)
    return HttpResponse(data, "image/png")

def checkname(request):
    name = request.POST.get("username")
    result = User.objects.filter(username=name)
    if result:
        return HttpResponse("error")
    return HttpResponse("ok")


def checkcapt(request):
    capt = request.POST.get("captcha")
    codes = request.session.get("codes")
    if capt.lower() == codes.lower():
        return HttpResponse("ok")
    return HttpResponse("error")


