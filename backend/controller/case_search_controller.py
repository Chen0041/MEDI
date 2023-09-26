from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.service import medical_case_service, case_search_service

import json


# Prepare For Case Search
@csrf_exempt
@require_http_methods(["POST"])
def case_search_preparation(request, caseId: int):
    print(caseId)
    medical_case_entity = medical_case_service.get_medical_case_by_id(caseId)
    return HttpResponse(json.dumps(medical_case_entity), content_type="application/json")
    # medicalCaseEntity = ocrService.ocrMedicalCase(medicalCaseEntity);
    # Long kdId = caseSearchService.createGraph(medicalCaseEntity);


# Get Similar Graphs From The Given KG
@csrf_exempt
@require_http_methods(["GET"])
def get_similar_graphs(request, kdId: int):
    print(kdId)
    similar_graphs = case_search_service.get_similar_graphs(kdId)
    return HttpResponse("success", content_type="application/json")


# Get NoteEvents By hadmId
@csrf_exempt
@require_http_methods(["GET"])
def get_note_events(request, hadmId: str):
    print(hadmId)
    return HttpResponse("success", content_type="application/json")
