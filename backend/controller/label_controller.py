import json
import os
from concurrent.futures._base import LOGGER

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse

@csrf_exempt
@require_http_methods(["POST"])
def done_labeling(dataset, request):
    try:
        # call_python(dataset);
        # backend/vqa_dataset_gene/generateVQA.py入口函数
        LOGGER.info(dataset)
    except Exception as e:
        LOGGER.error(str(e), e)
    return HttpResponse("success")
