from backend.models import Report


def get_all_models():
    models = list(Report.objects.filter(state='done'))
    return models
