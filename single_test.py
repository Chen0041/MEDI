# # 生成随机数
# import random
#
# random_alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# random_str = ''.join(random.choice(random_alphanumeric) for _ in range(15))
# print(random_str)
#
# # 文件重命名
import os
from MEDI.settings import project_path
#
# os.rename(project_path + 'backend/tests.py', project_path + 'backend/' + random_str + '.py')
#
# 文件相关操作
file = open(project_path + 'backend/tests.py')
file_name = str(file.name.split('/')[-1])
print(file_name)
print(file_name[-3:])  # 后缀

# 判断文件（夹）是否存在
if not os.path.exists(project_path+'test'):
    os.makedirs(project_path+'test')

# 文件拷贝
# with open(file.name, 'wb+') as f:
#     for chunk in file.chunks():
#         f.write(chunk)
#
# # 数据库查询API
# import json
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
#
# from backend.models import Dataset
# @csrf_exempt
# @require_http_methods(["GET"])
# def get_all_models(request):
#     # 查询后直接返回
#     ret = list(Dataset.objects.all().values())
#     # 进一步筛选
#     ret2 = []
#     for dataset in ret:
#         if dataset.islabeled == "0":
#             continue
#         ret2.append(dataset.name)
#     # 条件查询
#     ret3 = Dataset.objects.filter(status=0, islabeled="0").values()
#
#     return HttpResponse(json.dumps(ret2), content_type="application/json")
