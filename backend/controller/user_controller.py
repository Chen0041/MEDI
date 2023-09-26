from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods


# User log in
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    return None


# 用户注册
@csrf_exempt
@require_http_methods(["PUT"])
def user_register(request):
    return None


# 管理员获取所有用户信息
@csrf_exempt
@require_http_methods(["GET"])
def get_all_users(request):
    return None

# QA检索
@csrf_exempt
@require_http_methods(["POST"])
def search_simple_question(request):
    return None