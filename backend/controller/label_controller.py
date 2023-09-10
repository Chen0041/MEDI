import json
import os
from concurrent.futures._base import LOGGER

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse

from MEDI.settings import dataset_upload
from backend.models import CtValidation, CtInformation
from backend.vqa_dataset_gene import mysqlConnector


@csrf_exempt
@require_http_methods(["POST"])
def upload_label(request, dataset):
    patient_id = request.POST.get('description', default="")
    dia_list = request.POST.get('diaList', default="")
    photo_id = request.POST.get('photoId', default="")
    description = request.POST.get('description', default="")
    bone_name = request.POST.get('boneName', default="")
    direction = request.POST.get('direction', default="")
    type_ = request.POST.get('type', default="")
    position = request.POST.get('position', default="")
    if len(patient_id) == 0 or len(dia_list) == 0 or len(photo_id) == 0 or len(description) == 0 or \
            len(bone_name) == 0 or len(direction) == 0 or len(type_) == 0 or len(position) == 0:
        return HttpResponse("Invalid request parameters", status=400)
    else:
        ct_validation_po = CtValidation(patient_id=patient_id, photo_id=photo_id, dia_list=dia_list,
                                        description=description,
                                        bone_name=bone_name, direction=direction, type=type_, position=position,
                                        dataset=dataset)
        ct_validation_po.save()

        ct_information_po = CtInformation.objects.get(patient_id=patient_id, photo_id=photo_id, dataset=dataset)
        ct_information_po.status = 1
        ct_information_po.dia_list = dia_list
        ct_information_po.save()

        return HttpResponse("success")


@csrf_exempt
@require_http_methods(["POST"])
def done_labeling(request, dataset):
    try:
        VQApath = dataset_upload + "/" + dataset + "/VQA/"
        print(VQApath)
        mysqlConnector.setDatasetStatus(dataset, VQApath)
        LOGGER.info(dataset)
    except Exception as e:
        LOGGER.error(str(e), e)
    return HttpResponse("success")


@csrf_exempt
@require_http_methods(["GET"])
def get_all_patients(request, dataset):
    ctInfo_pos = list(CtInformation.objects.filter(status=0, dataset=dataset).values())
    print(ctInfo_pos)
    if len(ctInfo_pos) == 0:
        return HttpResponse(json.dumps(ctInfo_pos), content_type="application/json", status=460)
    else:
        return HttpResponse(json.dumps(ctInfo_pos), content_type="application/json", status=200)
