from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def consult_online(request):
    msg = request.POST.get('msg')
    return HttpResponse("success", content_type="application/json")
