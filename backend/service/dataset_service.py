from backend.dao import dataset_dao
from backend.models import Dataset


def get_all_datasets():
    return dataset_dao.get_dataset_pos()


def add_dataset(dataset_po: Dataset):
    dataset_dao.add_dataset(dataset_po)
