import json
import os
import shutil
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from MEDI.settings import project_path
from backend.service import train_model_service


@csrf_exempt
@require_http_methods(["GET"])
def get_all_models(request):
    models = train_model_service.get_all_models()
    print(models)
    return HttpResponse(json.dumps(models), content_type="application/json")


@csrf_exempt
@require_http_methods(["POST"])
def upload_medical_archive(request):
    model_name = request.POST.get('modelName')
    ques = request.POST.get('desc')
    file = request.FILES.get('file')
    print("upload imag to ai robot. Model: "+model_name);
    upload_path = project_path + "uploadimag"
    # 生成15位随机字母数字字符串
    random_alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_str = ''.join(random.choice(random_alphanumeric) for _ in range(15))

    file_name = file.name
    file_path = os.path.join(upload_path, random_str + file_name[-4:])
    print(file_path)

    # 判断父级目录是否存在
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)

    try:
        with open(upload_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        os.rename(upload_path+file_name, upload_path+random_str+file_name[-4:])
        print(upload_path+random_str+file_name[-4:])
        return HttpResponse("success")
    except IOError as e:
        print(e)
        return HttpResponse("error", status=400)
