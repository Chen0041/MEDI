from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def get_KG_list(request, userId: int):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def get_KG_by_id(request, kgId: int):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def get_random_KG(request):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def get_rel_nodes(request, nodeId: int):
    return None


@csrf_exempt
@require_http_methods(["POST"])
def create_graph(request):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def search_mode(request, node: str):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def get_node_and_rel_by_id(request, nodeId: int):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def get_statistics(request):
    return None


@csrf_exempt
@require_http_methods(["POST"])
def upload_KG(request, doctorId: int):
    return None