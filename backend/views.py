from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from backend.models import UserRole


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    user_role_list = UserRole.objects.order_by('user_id')[:5]
    output = ', '.join([str(r.role_id) for r in user_role_list])
    return HttpResponse(output)
