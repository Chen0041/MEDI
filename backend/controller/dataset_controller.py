import json
import os
from concurrent.futures._base import LOGGER

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse

from backend.models import Dataset
from backend.service import dataset_service
from backend.vqa_dataset_gene.main import main as python_main

from MEDI.settings import dataset_upload, frontend_static


@csrf_exempt
@require_http_methods(["GET"])
def get_datasets(request):
    datasets = dataset_service.get_all_datasets()
    return HttpResponse(json.dumps(datasets), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def get_all_names_labeled(request):
    dataset_pos = list(Dataset.objects.all())

    ret = []
    for dataset in dataset_pos:
        if dataset.islabeled == 0:
            continue
        ret.append(dataset.name)

    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_all_names(request):
    dataset_pos = list(Dataset.objects.all())

    ret = []
    for dataset in dataset_pos:
        print(dataset.name)
        if dataset.islabeled == 1:
            continue
        ret.append(dataset.name)

    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def add_dataset(request):
    name = request.POST.get('name', None)
    description = request.POST.get('description', None)
    train = request.POST.get('train', None)
    valid = request.POST.get('valid', None)
    test = request.POST.get('test', None)

    if len(name) == 0 or len(description) == 0 or train == 0 or valid is None or test == 0:
        return HttpResponse("Invalid request parameters", status=400)
    else:
        dataset_po = Dataset(name=name, description=description, islabeled=0, status=0, test=test, train=train,
                             valid=valid)
        dataset_service.add_dataset(dataset_po)
        return HttpResponse("Dataset added successfully")


@csrf_exempt
@require_http_methods(["POST"])
def upload(request):
    upload_file = request.FILES.get('file')
    if not upload_file:
        return JsonResponse({"error": "Upload failed, please choose a file"}, status=400)

    save_path = os.path.join(dataset_upload, upload_file.name)
    with open(save_path, 'wb+') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)

    try:
        python_main(save_path, frontend_static)
        # python_main(file_path, img_path)
        return HttpResponse("success")
    except Exception as e:
        LOGGER.error(str(e), e)
        return JsonResponse({"error": "Upload failed"}, status=400)
