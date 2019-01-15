from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


# 用来接收前端请求的模块,每个请求对应一个函数
# 所有请求信息默认都被封装到request对象中
def index(request):
    # return HttpResponse("hello django!!!")
    # 可以采用dict类型给index页面传递参数
    # 默认所有的页面都存储在templates目录中
    # return render(request, "index.html", {'hello': 'hello django'})

    # 1：调用业务逻辑类
    # 2：调用数据访问层，由于django采用orm映射，因此直接操作类即可
    articles = Article.objects.all()
    return render(request, "index.html", {'articles': articles})
