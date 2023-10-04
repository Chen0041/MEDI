import json
import jwt

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from backend.models import SysUser, QuestionTest


# User log in
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    login_vo = json.loads(request.body)
    if login_vo is None or login_vo['login_name'] == '' or login_vo['password'] == '':
        return HttpResponse('error username or password', status=401, content_type='application/json')
    else:
        user = SysUser.objects.get(login_name=login_vo['login_name'])
        if user is None or user.password != login_vo['password']:
            return HttpResponse('error username or password', status=401, content_type='application/json')
        token = jwt.encode({"login_name": login_vo['login_name']}, "secret", algorithm="HS256")
        info = json.dumps({"info": str(user.username), "type": user.type})
        response = HttpResponse(info, status=200, content_type='application/json')
        response.headers['token'] = bytes.decode(token)
        return response


# 用户注册，在SysUser数据库中新增记录
@csrf_exempt
@require_http_methods(["PUT"])
def user_register(request):
    user_entity = json.loads(request.body)
    print(user_entity)
    new_sys_user = SysUser(login_name=user_entity['login_name'], username=user_entity['username'],
                           password=user_entity['password'], age=user_entity['age'], gender=user_entity['gender'],
                           phone=user_entity['phone'], type=user_entity['type'], state=user_entity['state'],
                           email=user_entity['email'], identityid=user_entity['identityId'],
                           birthday=user_entity['birthday'], nation=user_entity['nation'],
                           marriage=user_entity['marriage'], birth_place=user_entity['birth_place'],
                           work_place=user_entity['work_place'])
    new_sys_user.save()
    return HttpResponse('success', status=200, content_type='application/json')


# no usage
# 管理员获取所有用户信息
# @csrf_exempt
# @require_http_methods(["GET"])
# def get_all_users(request):
#     return None


# QA检索
@csrf_exempt
@require_http_methods(["POST"])
def search_simple_question(request):
    question = request.POST.get('question')
    print(question)
    question_tests = QuestionTest.objects.all()
    doc = []
    for question_test in question_tests:
        doc.append(question_test.content)
    return None