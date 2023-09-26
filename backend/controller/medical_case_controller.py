from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Show clustering Result
@csrf_exempt
@require_http_methods(["GET"])
def get_cluster_result(request):
    return None


# Upload Dataset for clustering
@csrf_exempt
@require_http_methods(["POST"])
def upload_dataset_for_clustering(request):
    return None


# Get Medical Case List By User Id
# Upload Medical Case
@csrf_exempt
def get_case_list_or_upload_medical_case(request, userId: int):
    # GET and POST
    return None


# Upload Medical Case
@csrf_exempt
@require_http_methods(["POST"])
def upload_history_admissions(request, userId: int):
    return None


# Download Sample Csv For Clustering
@csrf_exempt
@require_http_methods(["POST"])
def download_sample_csv_file_for_cluster(request):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def download_sample_csv_file(request):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def download_cluster_report(request):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def download_sample_image_file(request):
    return None