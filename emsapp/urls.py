from django import urls
from django.urls import path
from emsapp import views

app_name = "emsapp"

urlpatterns = [
    path("emplist/",views.emplist,name="emplist"),

    path("addemp/",views.addemp,name="addemp"),
    path("addemplogic/",views.addemplogic,name="addemplogic"),

    path("deleteemp/",views.deleteemp,name="deleteemp"),

    path("updataemp/",views.updataemp,name="updataemp"),
    path("updataemplogic/",views.updataemplogic,name="updataemplogic"),
]