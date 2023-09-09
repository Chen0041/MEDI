from django.urls import path

from . import views
from .controller import dataset_controller, label_controller

urlpatterns = [
    # 加上每个 Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'
    path('', views.login),
    path('index', views.index),
    path('user/login', views.login),

    # dataset_controller
    path('dataSets', dataset_controller.get_datasets),
    path('dataSetsNames', dataset_controller.get_all_names),
    path('dataSetsNamesLabeled', dataset_controller.get_all_names_labeled),
    path('addDataset', dataset_controller.add_dataset),
    path('upload', dataset_controller.upload),

    # label_controller
    path('vqa/<str:dataset>', label_controller.upload_label),
    path('doneLabeling/<str:dataset>', label_controller.done_labeling),
    path('all/<str:dataset>', label_controller.get_all_patients),
]