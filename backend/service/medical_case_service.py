from backend.dao import medical_case_dao


def get_medical_case_by_id(caseId: int):
    return medical_case_dao.get_medical_case_by_id(caseId)