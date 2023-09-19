# import json
# from concurrent.futures._base import LOGGER
#
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
#
# from backend.service import train_model_service
#
#
# @csrf_exempt
# @require_http_methods(["GET"])
# # def get_all_datasets(request):
# # ArrayList<String> ret=new ArrayList<String>();
# # ret.add("VQA-Med-2019");
# # ret.add("VQA-RAD");
# # ret.add("MVQA");
# # return ret;
#
# @csrf_exempt
# @require_http_methods(["POST"])
# def set_train_error(request, name):
#     # throws IOException, ParseException
#     try:
#         train_model_service.set_train_error(name);
#         return HttpResponse("success")
#     except Exception as e:
#         LOGGER.error(str(e), e)
#         return HttpResponse("error", status=400)
#
#
# @csrf_exempt
# @require_http_methods(["POST"])
# def set_train_error(request, name):
#     # throws IOException, ParseException
#     try:
#         train_model_service.set_train_error(name);
#         return HttpResponse("success")
#     except Exception as e:
#         LOGGER.error(str(e), e)
#         return HttpResponse("error", status=400)
#
# @csrf_exempt
# @require_http_methods(["GET"])
# # def get_datasets(request):
# #     datasets = dataset_service.get_all_datasets()
# #     print(datasets)
# #     return HttpResponse( json.dumps(datasets), content_type="application/json")