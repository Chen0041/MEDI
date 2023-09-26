from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods


# 根据id删除question
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_question(request, qid: int):
    return None


# 根据问题id查找选择题答案
@csrf_exempt
@require_http_methods(["GET"])
def search_choice_answer_by_id(request, qid: int):
    return None


# 根据问题id查找所有的详细回答
@csrf_exempt
@require_http_methods(["GET"])
def search_detail_answer_by_id(request, qid: int):
    return None