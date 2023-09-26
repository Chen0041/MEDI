import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.models import Doctor, Question, DataSetsUpload


# 管理员获取所有医生信息
@csrf_exempt
@require_http_methods(["GET"])
def get_all_doctors(request):
    doctors = list(Doctor.objects.all().values())
    return HttpResponse(json.dumps(doctors), content_type="application/json")


# 医生获取问题，前端传入的VO对象注明回答与否、问题类型
@csrf_exempt
@require_http_methods(["GET"])
def get_filter_question(request, doctorId: int):
    # @RequestBody FilterQuestionVO
    questions = list(Question.objects.all().values())
    return HttpResponse(json.dumps(questions), content_type="application/json")


# 医生获取某一个科室下的未回答问题
@csrf_exempt
@require_http_methods(["GET"])
def get_questions_in_hos_department(request, uid: int, hdId: int):
    ret = []
    questions = list(Question.objects.filter(hospitaldepartmentid=hdId).values())
    question_answereds = list(Question.objects.filter(userid=uid).values())
    for question in questions:
        for question_answered in question_answereds:
            if question['qid'] == question_answered['qid']:
                continue
            ret.append(question)
    return HttpResponse(json.dumps(ret), content_type="application/json")


# 医生回答某个问题
@csrf_exempt
@require_http_methods(["POST"])
def insert_answer(request,  uid: int, qid: int):
    # @RequestBody AnswerQuestionVO
    # data = json.loads(request.body)
    return HttpResponse("success", content_type="application/json")


# 医生新建一个数据集
@csrf_exempt
@require_http_methods(["POST"])
def new_dataset(request,  doctorId: int):
    # @RequestBody DataSetsEntity
    # data = json.loads(request.body)
    return HttpResponse("success", content_type="application/json")


# 医生上传数据集
@csrf_exempt
@require_http_methods(["POST"])
def upload_dataset(request,  doctorId: int):
    # MultipartFile file, Integer dId, String type
    file = request.FILES.get("file")
    dId = request.POST.get("dId")
    type = request.POST.get("type")
    print(file, dId, type)
    return HttpResponse("success", content_type="application/json")


# 医生获取全部数据集
# @csrf_exempt
# @require_http_methods(["GET"])
# def get_datasets(request, doctorId: int):
#     datasets = list(DataSetsUpload.objects.filter(user_id=doctorId).values())
#     return HttpResponse(json.dumps(datasets), content_type="application/json")


# 医生获取可用数据集
@csrf_exempt
@require_http_methods(["GET"])
def get_available_datasets(request, doctorId: int):
    datasets = list(DataSetsUpload.objects.filter(user_id=doctorId).values())
    return HttpResponse(json.dumps(datasets), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def do_deep_model_task(request, doctorId: int):
    # @RequestBody DeepModelTaskEntity
    return HttpResponse("success", content_type="application/json")
