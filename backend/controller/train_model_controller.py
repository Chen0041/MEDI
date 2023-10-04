import logging
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.models import Report
from backend.service import train_model_service


@csrf_exempt
@require_http_methods(["POST"])
def set_train_error(request, name):
    try:
        # report_po = Report.objects.get(name=name)
        # report_po.state = 'failed'
        # report_po.save()
        return HttpResponse("success", content_type="application/json")
    except Exception as e:
        logging.error(str(e))
        return HttpResponse("error! update report by name in dao.", status=400, content_type="application/json")


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_failed(request):
    try:
        Report.objects.filter(state='failed').delete()
        return HttpResponse("success", content_type="application/json")
    except Exception as e:
        logging.error(str(e))
        return HttpResponse("error! delete failed models in dao.", status=400, content_type="application/json")

# @csrf_exempt
# @require_http_methods(["POST"])
# def insert_report(request, model):
#     try:
#         report_vo_form = ReportVoForm(request.POST)
#         if report_vo_form.is_valid():
#             report_vo = report_vo_form.save()
#             # report_vo即为ReportVo对象 待测试
#     except Exception as e:
#         logging.error(str(e))
#         return HttpResponse("error!", status=400, content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def get_reports(request):
    report_pos = list(Report.objects.all().values())
    ret = []
    for report_po in report_pos:
        report_po['date'] = report_po['date'].strftime("%Y-%m-%d")
        # print(report_po['date'])
        ret.append(report_po)
    return HttpResponse(json.dumps(ret), content_type="application/json")

