from django.urls import path

from . import views

urlpatterns = [
    # 加上每个Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('user/login', views.login, name='login'),
]