from backend.dao import auto_diagnosis_dao, doctor_diagnosis_dao


def get_similar_graphs(kId: int):
    similar_graphs = auto_diagnosis_dao.get_similar_graphs(kId)
    if similar_graphs:
        return list(similar_graphs['similar_graphs'].split(","))
    else:
        # TODO
        pass


def get_doctor_diagnosis(admissionId: int):
    doctor_diagnosis = doctor_diagnosis_dao.get_doctor_diagnosis(admissionId)
    if len(doctor_diagnosis) == 0:
        return ''
    else:
        return doctor_diagnosis[0]['doctor_diagnosis']



