from django.urls import path

from . import views
from .controller import dataset_controller, label_controller

urlpatterns = [
    # 加上每个 Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'
    # name一般是YYY，出错可以参考前端 vue文件
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('user/login', views.login, name='login'),

    # dataset_controller
    path('dataSets', dataset_controller.get_datasets, name='dataSets'),
    path('dataSetsNames', dataset_controller.get_all_names, name='dataSetsNames'),
    path('dataSetsNamesLabeled', dataset_controller.get_all_names_labeled, name='dataSetsNamesLabeled'),
    path('addDataset', dataset_controller.add_dataset, name='addDataset'),
    path('upload', dataset_controller.upload, name='upload'),

    # label_controller
    path('doneLabeling/<str:dataset>/', label_controller.done_labeling, name='doneLabeling')
]