from django import urls
from django.urls import path
from login_regist_app import views

app_name = "login_regist_app"

urlpatterns = [
    path("login/",views.login,name="login"),
    path("loginlogic/",views.loginlogic,name="loginlogic"),

    path("regist/",views.regist,name="regist"),
    path("registlogic/",views.registlogic,name = "registlogic"),

    path("getcaptcha/",views.getcaptcha,name="getcaptcha"),

    path("checkname/",views.checkname,name="checkname"),
    path("checkcapt/",views.checkcapt,name="checkcapt"),
]