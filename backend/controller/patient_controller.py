from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods


# 病人查找自己提交的所有问题
@csrf_exempt
@require_http_methods(["GET"])
def search_my_question(request, patientId: int):
    return None


# 管理员获取所有病人信息
# 新增question
@csrf_exempt
def get_all_patients_or_add_question(request):
    # GET AND PUT
    return None