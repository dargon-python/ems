from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        if 'login' in request.path or 'regist' in request.path:
            pass
        else:
            status = request.session.get("status")
            if status:
                pass
            elif 'addemp' in request.path:
                url = reverse('login_regist_app:login')+'?addurl='+'addurl'
                return redirect(url)
            else:
                return redirect("login_regist_app:login")


    # # 在process_request之后View之前执行
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("view:", request, view_func, view_args, view_kwargs)
    #
    # # view执行之后，响应之前执行
    # def process_response(self, request, response):
    #     print("response:", request, response)
    #     return response  # 必须返回response
    #
    # # 如果View中抛出了异常
    # def process_exception(self, request, ex):  # View中出现异常时执行
    #     print("exception:", request, ex)