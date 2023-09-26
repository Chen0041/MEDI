from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse

from backend.service import auto_diagnosis_service

import json


@csrf_exempt
@require_http_methods(["POST"])
def diagnosis_preparation(request, archiveId: int):
    print(archiveId)
    return HttpResponse("success", content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_similar_graphs(request, kdId: int):
    # print(kdId)
    similar_graphs = auto_diagnosis_service.get_similar_graphs(kdId)
    return HttpResponse(json.dumps(similar_graphs), content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_doctor_diagnosis(request, admissionId: int):
    print(admissionId)
    doctor_diagnosis = auto_diagnosis_service.get_doctor_diagnosis(admissionId)
    return HttpResponse(json.dumps(doctor_diagnosis), content_type="application/json")
