from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
def get_archive_list_or_upload_medical_archive(request, userId: int):
    # GET and POST
    return None


@csrf_exempt
@require_http_methods(["GET"])
def download_medical_archive(request,  archiveId: int):
    return None