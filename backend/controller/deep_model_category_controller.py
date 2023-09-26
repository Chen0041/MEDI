import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.models import DeepModelCategory, DeepModel


def new_DeepModelCategory_value_format(deep_model_category):
    return {
        "id": deep_model_category['id'],
        "name": deep_model_category['category'],
        "models": deep_model_category['id']
    }


# 获取所有深度学习模型的类别
@csrf_exempt
@require_http_methods(["GET"])
def get_all_model_category(request):
    deep_model_category = list(DeepModelCategory.objects.all().values())
    ret = []
    for deep_model_category_item in deep_model_category:
        print(deep_model_category_item)
        ret.append(new_DeepModelCategory_value_format(deep_model_category_item))
    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


# Get All Deep Models (Only Model id and name)
@csrf_exempt
@require_http_methods(["GET"])
def get_deep_models_name(request):
    deep_model = list(DeepModel.objects.all().values())
    ret = []
    for deep_model_item in deep_model:
        ret.append({deep_model_item['id'], deep_model_item['model_name']})
    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


# 根据 id 获取模型信息
@csrf_exempt
@require_http_methods(["GET"])
def get_model_by_id(request, mId: int):
    print(mId)
    deep_models = list(DeepModel.objects.filter(id=mId).values())
    return HttpResponse(json.dumps(deep_models), content_type="application/json")
