import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.models import DeepModelMetric

# 获取所有模型评价指标
@csrf_exempt
@require_http_methods(["GET"])
def get_metrics(request):
    metrics = list(DeepModelMetric.objects.all().values())
    return HttpResponse(json.dumps(metrics), content_type="application/json")