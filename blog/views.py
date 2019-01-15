from django.shortcuts import render
from django.http import HttpResponse

# 用来接收前端请求的模块,每个请求对应一个函数
# 所有请求信息默认都被封装到request对象中
def index(request):
    # return HttpResponse("hello django!!!")
    # 可以采用dict类型给index页面传递参数
    # 默认所有的页面都存储在templates目录中
    return render(request, "index.html", {'hello': 'hello django'})
