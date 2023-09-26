import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.models import Doctor, Department


# 根据科室id获取科室下所有医生
@csrf_exempt
@require_http_methods(["GET"])
def get_doctors_by_department(request, did: int):
    doctors = list(Doctor.objects.filter(department=did).values())
    return HttpResponse(json.dumps(doctors), content_type="application/json")


# 获取所有科室
@csrf_exempt
@require_http_methods(["GET"])
def get_all_department(request):
    departments = list(Department.objects.all().values())
    return HttpResponse(json.dumps(departments), content_type="application/json")