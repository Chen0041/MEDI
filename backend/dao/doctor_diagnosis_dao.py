from backend.models import DoctorDiagnosis


def get_doctor_diagnosis(admissionId: int):
    doctor_diagnosis = list(DoctorDiagnosis.objects.filter(admissionid=admissionId))
    return doctor_diagnosis
