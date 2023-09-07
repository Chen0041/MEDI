from django.urls import path

from . import views
from .controller import dataset_controller

urlpatterns = [
    # 加上每个 Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'
    # name一般是YYY，出错可以参考前端 vue文件
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('user/login', views.login, name='login'),

    path('dataSets', dataset_controller.get_datasets, name='dataSets'),
    path('addDataset', dataset_controller.add_dataset, name='addDataset'),
    path('upload', dataset_controller.upload, name='upload')


]