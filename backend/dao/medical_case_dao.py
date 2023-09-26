from backend.models import MedicalArchive


def get_medical_case_by_id(caseId: int):
    # missing database, use MedicalArchive to replace currently
    return MedicalArchive.objects.get(id=caseId)