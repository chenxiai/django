from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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


def delete(request, article_id):
    # 通过ID获取对象,然后删除
    try:
        Article.objects.get(id=article_id).delete()
    except Exception:
        print('此处是处理异常的代码')
    articles = Article.objects.all()
    return render(request, "index.html", {'articles': articles})


def get_id(request, id):
    article = Article.objects.get(id=id)
    # 跳转到更新页面,数据实现回显
    return render(request, "update.html", {'article': article})

def update(request):
    # id 应该和前面隐藏域name相同
    id = request.POST.get('id')
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # 可以采用重定向跳转到index.html页面
    # /index/ 是去urls中找到合适的匹配路径
    return HttpResponseRedirect('/index/')
