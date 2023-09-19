from backend.models import Report
from backend.service import train_model_service


def get_all_models():
    return  train_model_service.get_all_models()
