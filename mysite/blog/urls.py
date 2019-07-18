from django.urls import include, path
from . import views

urlpatterns = [
    path('helloworld',views.helloworld),
    path('', views.index),
    path('index', views.index),
    path('detail/<int:article_id>', views.get_detail_page),
]