from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.

# api test
@csrf_exempt
def hello(request):
    dictdata = {'result':200,'msg':'haha连接成功'}
    #return JsonResponse(dictdata,charset='utf-8')
    return HttpResponse(json.dumps(dictdata, ensure_ascii=False), content_type="application/json,charset=utf-8")

def login(request):
    return render(request, "blog/login.html")

def loginverify(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if models.User.objects.filter(username=username):
        if models.User.objects.filter(username=username,password=password):
            return redirect('blog:index')
        else:
            return render(request, "blog/login.html",
                            {
                                'message': 'password filed!'
                            }

                         )
    else:
        return render(request, "blog/login.html" ,{
                            'message':'username not exists!'
                        }

                     )




# 表单
def search_form(request):
    return render(request,'blog/search_form.html')


# 接收请求数据
def search(request):
    #request.encoding = 'utf-8'
    q = request.POST.get('q')

    if q == '123':
        return redirect('blog:index')
    else:
        return redirect('blog:login')


def index(request):
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1

    username = request.POST.get('username')
    articles = models.Article.objects.all()
    top5_article_list=models.Article.objects.order_by('-article_id')[:3]
    paginator = Paginator(articles,4)

    page_num=paginator.num_pages
    page_article_list=paginator.page(page)
    if page_article_list.has_next():
        next_page=page+1
    else:
        next_page=page

    if page_article_list.has_previous():
        previous_page=page-1
    else:
        previous_page=page
    return render(request, 'blog/index.html',
                      {
                          'articles':page_article_list,
                          'page_num':range(1,page_num+1),
                          'curr_page':page,
                          'next_page':next_page,
                          'previous_page':previous_page,
                          'top5_article_list':top5_article_list,
                          'username':username,
                      }
                 )

def get_detail_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    filter_previous_article=models.Article.objects.filter(article_id__lte=article_id)
    filter_next_article=models.Article.objects.filter(article_id__gte=article_id)
    if len(filter_previous_article)==1:
        previous_article=filter_previous_article[len(filter_previous_article)-1]
    else:
        previous_article=filter_previous_article[len(filter_previous_article)-2]

    if len(filter_next_article)==1:
        next_article=filter_next_article[0]
    else:
        next_article=filter_next_article[1]




    return render(request, 'blog/detail.html',
                      {
                          'article':article,
                          'previous_article':previous_article,
                          'next_article':next_article
                      }
                 )

