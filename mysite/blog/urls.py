from django.urls import include, path, reverse
from . import views

app_name = 'blog'
urlpatterns = [
    path('hello',views.hello),
    path('login', views.login, name = 'login'),
    path('loginverify', views.loginverify, name = 'loginverify'),

    path('search_form', views.search_form, name = 'search_form'),
    path('search', views.search, name = 'search'),


    path('', views.index, name = 'index'),
    path(r'index(?page=<int:previous_page>)/', views.index,name = 'page_index'),
    path('detail/<int:article_id>/', views.get_detail_page,name = 'detail'),
]