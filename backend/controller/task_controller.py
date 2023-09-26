from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def download_auto_selection_task_result(request, taskId: int):
    return None


@csrf_exempt
@require_http_methods(["GET"])
def download_knowledge_exploration_task_result(request, taskId: int):
    return None


# Get Model Evaluation Task Result
@csrf_exempt
@require_http_methods(["GET"])
def get_model_evaluation_task_result(request,  taskId: int):
    return None


# Get Auto Selection Task Results
@csrf_exempt
@require_http_methods(["GET"])
def get_auto_selection_task_result(request, taskId: int):
    return None


# Get Knowledge Exploration Task Results
@csrf_exempt
@require_http_methods(["GET"])
def get_knowledge_exploration_task_result(request, taskId: int):
    return None


# Get all Model Evaluation Tasks
# Add A Model Evaluation Task
@csrf_exempt
def get_or_add_model_evaluation_tasks(request, doctorId: int):
    #GET AND POST
    return None


# Get all Auto Selection Tasks
# Add A Auto Selection Task
@csrf_exempt
def get_or_add_auto_selection_tasks(request,  doctorId: int):
    # GET AND POST
    return None


# Get all Knowledge-Embedding Exploration Tasks
# Add A Knowledge-Embedding Exploration Task
@csrf_exempt
def get_or_add_knowledge_embedding_exploration_tasks(request, doctorId: int):
    # GET AND POST
    return None