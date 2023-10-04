import json
import logging

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from MEDI.settings import project_path
from backend.models import CtValidation, CtInformation, Dataset


@csrf_exempt
@require_http_methods(["POST"])
def upload_label(request, dataset):
    patient_id = request.POST.get('patientId', default="")
    dia_list = request.POST.get('diaList', default="")
    photo_id = request.POST.get('photoId', default="")
    description = request.POST.get('description', default="")
    bone_name = request.POST.get('boneName', default="")
    direction = request.POST.get('direction', default="")
    type_ = request.POST.get('type', default="")
    position = request.POST.get('position', default="")
    if len(patient_id) == 0 or len(dia_list) == 0 or len(photo_id) == 0 or len(description) == 0 or \
            len(bone_name) == 0 or len(direction) == 0 or len(type_) == 0 or len(position) == 0:
        return HttpResponse("Invalid request parameters", status=400, content_type="application/json")
    else:
        ct_validation_po = CtValidation(patient_id=patient_id, photo_id=photo_id, dia_list=dia_list,
                                        description=description,
                                        bone_name=bone_name, direction=direction, type=type_, position=position,
                                        dataset=dataset)
        ct_validation_po.save()

        ct_information_po = CtInformation.objects.get(patient_id=patient_id, photo_id=photo_id, dataset=dataset)
        ct_information_po.status = '1'
        ct_information_po.save()

        return HttpResponse("success", content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def done_labeling(request, dataset):
    try:
        VQApath = project_path + "VQAdataset/" + dataset + "/VQA/"
        dataset = Dataset.objects.get(name=dataset)
        dataset.status = 1
        dataset.link = VQApath
        dataset.save()
        return HttpResponse("success", content_type="application/json")
    except Exception as e:
        logging.error(str(e), e)
        return HttpResponse("error", status=400, content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_all_patients(request, dataset):
    ctInfo_pos = list(CtInformation.objects.filter(status='0', dataset=dataset).values())
    # print(ctInfo_pos)
    if len(ctInfo_pos) == 0:
        return HttpResponse(json.dumps(ctInfo_pos), content_type="application/json", status=460)
    else:
        return HttpResponse(json.dumps(ctInfo_pos), content_type="application/json", status=200)
