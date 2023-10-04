from django.urls import path

from . import views
from .controller import dataset_controller, label_controller, consult_VQA_controller, train_model_controller, \
    auto_diagnosis_controller, case_search_controller, consult_controller, deep_model_category_controller, \
    deep_model_metric_controller, department_controller, doctor_controller, KG_controller, medical_archive_controller, \
    medical_case_controller, patient_controller, preprocess_controller, QA_controller, task_controller, user_controller

urlpatterns = [
    # 加上每个 Controller文件开头的 @RequestMapping("XXX")
    # 格式：'XXX/YYY'，前后没有'/'

    # path('', views.login),
    path('singleTest', dataset_controller.single_test),

    # consult_VQA_controller
    path('models', consult_VQA_controller.get_all_models),
    # TODO:python
    # path('archive/user/<str:modelName>', consult_VQA_controller.upload_medical_archive),

    # dataset_controller
    path('dataSets', dataset_controller.get_datasets),
    path('dataSetsNames', dataset_controller.get_all_names),
    path('dataSetsNamesLabeled', dataset_controller.get_all_names_labeled),
    path('addDataset', dataset_controller.add_dataset),
    # TODO: zh python
    path('upload', dataset_controller.upload),

    # label_controller
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

    # auto_diagnosis_controller
    # TODO: about all
    path('diagnosis/<int:archiveId>', auto_diagnosis_controller.diagnosis_preparation),
    # TODO: about all
    path('diagnosis/<int:kdId>', auto_diagnosis_controller.get_similar_graphs),
    # TODO: TEST
    path('diagnosis/admission/<int:admissionId>', auto_diagnosis_controller.get_doctor_diagnosis),

    # case_search_controller
    # TODO: about all, database
    path('caseSearch/<int:caseId>', case_search_controller.case_search_preparation),
    # TODO: database
    path('caseSearch/<int:kdId>', case_search_controller.get_similar_graphs),
    # TODO: database
    path('caseSearch/history_admissions/<str:hadmId>', case_search_controller.get_note_events),

    # consult_controller
    # TODO: about all
    path('consult/online', consult_controller.consult_online),

    # deep_model_category_controller
    # TODO: TEST
    path('modelCategory', deep_model_category_controller.get_all_model_category),
    # TODO: TEST
    path('modelCategory/modelName', deep_model_category_controller.get_deep_models_name),
    # TODO: TEST
    path('modelCategory/model/<int:mId>', deep_model_category_controller.get_model_by_id),

    # deep_model_metric_controller
    # TODO: TEST
    path('modelMetric', deep_model_metric_controller.get_metrics),

    # department_controller
    # TODO: TEST
    path('department/<int:did>/doctor', department_controller.get_doctors_by_department),
    # TODO: TEST
    path('department', department_controller.get_all_department),

    # doctor_controller
    # TODO: TEST
    path('doctor', doctor_controller.get_all_doctors),
    # TODO: VO
    # path('doctor/<int:doctorId>/question', doctor_controller.get_filter_question),
    # TODO: TEST
    path('doctor/<int:uid>/question/hospitalDepartment/<int:hdId>', doctor_controller.get_questions_in_hos_department),
    # TODO: VO
    # path('doctor/<int:uid>/question/<int:qid>/answer', doctor_controller.insert_answer),
    # TODO: VO
    # path('doctor/<int:doctorId>/dataSet', doctor_controller.new_dataset),
    # TODO: file POST OR double? related to availableDataSets
    # path('doctor/<int:doctorId>/dataSets', doctor_controller.upload_dataset),
    # TODO: TEST
    path('doctor/<int:doctorId>/availableDataSets', doctor_controller.get_available_datasets),
    # only POST TODO: VO
    # path('doctor/<int:doctorId>/DLTask', doctor_controller.do_deep_model_task),

    # KG_controller
    path('kg/user/<int:userId>', KG_controller.get_KG_list),
    path('kg/graph/<int:kgId>', KG_controller.get_KG_by_id),
    path('kg/graph', KG_controller.get_random_KG),
    path('kg/graph/relNodes/<int:nodeId>', KG_controller.get_rel_nodes),
    path('kg/creatGraph', KG_controller.create_graph),
    path('kg/node/search/<str:node>', KG_controller.search_mode),
    path('kg/node/<int:nodeId>', KG_controller.get_node_and_rel_by_id),
    path('kg/statistics', KG_controller.get_statistics),
    path('kg/upload/<int:doctorId>', KG_controller.upload_KG),

    # medical_archive_controller
    path('archive/user/<int:userId>', medical_archive_controller.get_archive_list_or_upload_medical_archive),
    path('archive/download/<int:archiveId>', medical_archive_controller.download_medical_archive),

    # medical_case_controller
    path('case/cluster/result', medical_case_controller.get_cluster_result),
    path('case/dataset/<int:userId>', medical_case_controller.upload_dataset_for_clustering),
    path('case/user/<int:userId>', medical_case_controller.get_case_list_or_upload_medical_case),
    path('case/history_admissions/<int:userId>', medical_case_controller.upload_history_admissions),
    path('case/download/SampleCsvFileForCluster', medical_case_controller.download_sample_csv_file_for_cluster),
    path('case/download/SampleCsvFile', medical_case_controller.download_sample_csv_file),
    path('case/download/ClusterReport', medical_case_controller.download_cluster_report),
    path('case/download/SampleImageFile', medical_case_controller.download_sample_image_file),

    # patient_controller
    path('patient/<int:patientId>/question', patient_controller.search_my_question),
    path('patient', patient_controller.get_all_patients_or_add_question),

    # preprocess_controller
    path('preprocess/<int:archiveId>', preprocess_controller.preprocess_medical_archive),

    # QA_controller
    path('QA/<int:qid>', QA_controller.delete_question),
    path('QA/<int:qid>/simpleAnswer', QA_controller.search_choice_answer_by_id),
    path('QA/<int:qid>/detailAnswer', QA_controller.search_detail_answer_by_id),

    # task_controller
    path('task/autoSelection/downloadResult/<int:taskId>', task_controller.download_auto_selection_task_result),
    path('task/knowledgeExploration/downloadResult/<int:taskId>', task_controller.download_knowledge_exploration_task_result),
    path('task/modelEvaluationResult/<int:taskId>', task_controller.get_model_evaluation_task_result),
    path('task/autoSelectionResult/<int:taskId>', task_controller.get_auto_selection_task_result),
    path('task/knowledgeExplorationResult/<int:taskId>', task_controller.get_knowledge_exploration_task_result),
    path('task/<int:doctorId>/modelEvaluation', task_controller.get_or_add_model_evaluation_tasks),
    path('task/<int:doctorId>/autoSelection', task_controller.get_or_add_auto_selection_tasks),
    path('task/<int:doctorId>/knowledgeExploration', task_controller.get_or_add_knowledge_embedding_exploration_tasks),

    # user_controller
    path('user/login', user_controller.login),
    path('user/register', user_controller.user_register),
    # path('user', user_controller.get_all_users), no usage
    # TODO: Q&A Question search
    path('user/similarityQuestion', user_controller.search_simple_question),
]
