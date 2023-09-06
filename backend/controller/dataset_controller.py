import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from backend.service import dataset_service


@csrf_exempt
@require_http_methods(["GET"])
def get_datasets(request):
    print("Get datasets.")
    datasets = dataset_service.get_all_datasets()
    return HttpResponse(json.dumps(datasets), content_type="application/json")


