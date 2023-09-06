from backend.models import Dataset


def get_dataset_pos():
    query = list(Dataset.objects.values())
    return query


def add_dataset(dataset: Dataset):
    dataset.save()
