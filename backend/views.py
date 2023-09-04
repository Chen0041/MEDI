from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# from django.http import JsonResponse
import json

from backend.models import UserRole


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    print("login")
    # data
    data = json.loads(request.body.decode('utf-8'))
    print(data.get('login_name'))
    print(data.get('password'))
    # MySQL dataset
    user_role_list = UserRole.objects.order_by('user_id')[:5]
    output = '<br/> '.join(['use_id: ' + str(r.user_id) + ', role_id: ' + str(r.role_id) for r in user_role_list])
    return HttpResponse(output)
