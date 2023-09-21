from django.urls import path

from . import views
from .controller import dataset_controller, label_controller, consult_VQA_controller, train_model_controller

urlpatterns = [
    # 加上每个 Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'
    # path('', views.login),
    # path('index', views.index),
    # path('user/login', views.login),

    # consult_VQA_controller
    path('models', consult_VQA_controller.get_all_models),
    # TODO:python
    # path('archive/user/<str:modelName>', consult_VQA_controller.upload_medical_archive),

    # dataset_controller
    path('dataSets', dataset_controller.get_datasets),
    path('dataSetsNames', dataset_controller.get_all_names),
    path('dataSetsNamesLabeled', dataset_controller.get_all_names_labeled),
    path('addDataset', dataset_controller.add_dataset),
    # TODO:python
    path('upload', dataset_controller.upload),

    # label_controller
    # TODO:test
    path('vqa/<str:dataset>', label_controller.upload_label),  # label.vue
    # TODO:python
    path('doneLabeling/<str:dataset>', label_controller.done_labeling),
    path('all/<str:dataset>', label_controller.get_all_patients),

    # train_model_controller
    # TODO:test
    path('error/<str:name>', train_model_controller.set_train_error),
    # TODO:test
    path('deleteFailed', train_model_controller.delete_failed),
    # TODO:about all
    # path('train/<str:model>', train_model_controller.insert_report),
    path('reports', train_model_controller.get_reports),
    # TODO:file, about all
    # path('downloadReports', train_model_controller.download_file),
]
