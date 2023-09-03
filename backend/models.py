# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoSelectionTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dataset_id = models.BigIntegerField(blank=True, null=True)
    metric_id = models.IntegerField(blank=True, null=True)
    query_length = models.IntegerField(blank=True, null=True)
    document_length = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('SysUser', models.DO_NOTHING, blank=True, null=True)
    result_file = models.CharField(max_length=255, blank=True, null=True)
    result_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_selection_task'


class CtInformation(models.Model):
    patient_id = models.CharField(max_length=255, blank=True, null=True)
    sym = models.CharField(max_length=1000, blank=True, null=True)
    photo_id = models.CharField(max_length=255, blank=True, null=True)
    dia_list = models.CharField(max_length=1000, blank=True, null=True)
    annotation = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    dataset = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_information'


class CtValidation(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_id = models.CharField(max_length=255, blank=True, null=True)
    photo_id = models.CharField(max_length=255, blank=True, null=True)
    dia_list = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    bone_name = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    dataset = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_validation'


class DataSetsUpload(models.Model):
    dataset_name = models.CharField(max_length=255)
    dataset_desc = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    train_path = models.CharField(max_length=255, blank=True, null=True)
    train_name = models.CharField(max_length=255, blank=True, null=True)
    test_path = models.CharField(max_length=255, blank=True, null=True)
    test_name = models.CharField(max_length=255, blank=True, null=True)
    dev_path = models.CharField(max_length=255, blank=True, null=True)
    dev_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_sets_upload'


class Dataset(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    status = models.IntegerField()
    link = models.CharField(max_length=300, blank=True, null=True)
    islabeled = models.CharField(max_length=4, blank=True, null=True)
    test = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    train = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataset'


class DeepModel(models.Model):
    model_name = models.CharField(max_length=255, blank=True, null=True)
    model_introduction = models.TextField(blank=True, null=True)
    model_article_title = models.CharField(max_length=255, blank=True, null=True)
    model_article_url = models.CharField(max_length=255, blank=True, null=True)
    model_architecture_url = models.CharField(max_length=255, blank=True, null=True)
    model_code_url = models.CharField(max_length=255, blank=True, null=True)
    model_category = models.ForeignKey('DeepModelCategory', models.DO_NOTHING, db_column='model_category', blank=True, null=True)
    config_file = models.CharField(max_length=255, blank=True, null=True)
    model_py = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deep_model'


class DeepModelCategory(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deep_model_category'


class DeepModelMetric(models.Model):
    metric = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deep_model_metric'


class DeepModelTaskResult(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    model_id = models.BigIntegerField(blank=True, null=True)
    ndcg_1 = models.CharField(db_column='ndcg@1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ndcg_3 = models.CharField(db_column='ndcg@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ndcg_5 = models.CharField(db_column='ndcg@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ndcg_10 = models.CharField(db_column='ndcg@10', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    map = models.CharField(max_length=255, blank=True, null=True)
    recall_3 = models.CharField(db_column='recall@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    recall_5 = models.CharField(db_column='recall@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    recall_10 = models.CharField(db_column='recall@10', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pre_1 = models.CharField(db_column='pre@1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pre_3 = models.CharField(db_column='pre@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pre_5 = models.CharField(db_column='pre@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pre_10 = models.CharField(db_column='pre@10', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'deep_model_task_result'


class Department(models.Model):
    hdid = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    identityid = models.CharField(db_column='identityID', max_length=18)  # Field name made lowercase.
    birthday = models.CharField(max_length=10, blank=True, null=True)
    marriage = models.CharField(max_length=2, blank=True, null=True)
    nation = models.CharField(max_length=20, blank=True, null=True)
    birth_place = models.CharField(max_length=30, blank=True, null=True)
    work_place = models.CharField(max_length=30, blank=True, null=True)
    entry_time = models.CharField(max_length=10, blank=True, null=True)
    department = models.BigIntegerField(blank=True, null=True)
    duty = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    skill = models.CharField(max_length=500, blank=True, null=True)
    outpatient_time = models.CharField(max_length=500, blank=True, null=True)
    introduction = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'
        unique_together = (('id', 'identityid'),)


class DoctorDiagnosis(models.Model):
    admission_id = models.IntegerField()
    doctor_diagnosis = models.CharField(max_length=16384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_diagnosis'


class Expert(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    identityid = models.CharField(db_column='identityID', max_length=255)  # Field name made lowercase.
    birthday = models.CharField(max_length=10, blank=True, null=True)
    marriage = models.CharField(max_length=4, blank=True, null=True)
    nation = models.CharField(max_length=25, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    work_place = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.CharField(max_length=250, blank=True, null=True)
    introduction = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expert'


class Kg(models.Model):
    kg_name = models.CharField(max_length=255, blank=True, null=True)
    kg_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kg'


class KgUpload(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    kg_desc = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kg_upload'


class KnowledgeEmbeddingExplorationTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dataset_id = models.BigIntegerField(blank=True, null=True)
    metric_id = models.BigIntegerField(blank=True, null=True)
    query_length = models.IntegerField(blank=True, null=True)
    document_length = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    result_id = models.BigIntegerField(blank=True, null=True)
    result_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge_embedding_exploration_task'


class MedicalArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.IntegerField()
    zip_file_path = models.CharField(max_length=255)
    txt_file_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_archive'


class ModelEvaluationTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    dataset_id = models.IntegerField(blank=True, null=True)
    query_length = models.IntegerField(blank=True, null=True)
    document_length = models.IntegerField(blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    metric_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('SysUser', models.DO_NOTHING, blank=True, null=True)
    result_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_evaluation_task'


class Patient(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    birthday = models.CharField(max_length=10, blank=True, null=True)
    marriage = models.CharField(max_length=2, blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)
    birth_place = models.CharField(max_length=30, blank=True, null=True)
    work_place = models.CharField(max_length=30, blank=True, null=True)
    contact_person = models.CharField(max_length=20, blank=True, null=True)
    contact_phone = models.CharField(max_length=11, blank=True, null=True)
    contact_relationship = models.CharField(max_length=10, blank=True, null=True)
    contact_address = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    medicare_card_id = models.CharField(max_length=15, blank=True, null=True)
    identityid = models.CharField(db_column='identityID', max_length=18)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'
        unique_together = (('id', 'identityid'),)


class Permission(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    url = models.CharField(max_length=256, db_collation='utf8mb3_general_ci')
    handle = models.CharField(max_length=20, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'permission'


class Question(models.Model):
    qid = models.BigAutoField(primary_key=True)
    content = models.TextField()
    hospitaldepartmentid = models.BigIntegerField(db_column='hospitalDepartmentId')  # Field name made lowercase.
    type = models.IntegerField()
    userid = models.BigIntegerField()
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionDetailAnswer(models.Model):
    qrid = models.BigAutoField(primary_key=True)
    qid = models.BigIntegerField()
    user_id = models.BigIntegerField()
    detail_answer = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_detail_answer'


class QuestionTest(models.Model):
    content = models.TextField(blank=True, null=True)
    hospitaldepartmentid = models.IntegerField(db_column='hospitalDepartmentId', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_test'


class Questionresult(models.Model):
    qrid = models.BigAutoField(primary_key=True)
    questionid = models.ForeignKey(Question, models.DO_NOTHING, db_column='questionid')
    userid = models.ForeignKey('SysUser', models.DO_NOTHING, db_column='userid')
    resulttype = models.IntegerField(db_column='resultType', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionresult'


class Report(models.Model):
    name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    data = models.CharField(max_length=20, blank=True, null=True)
    savepath = models.CharField(max_length=256, blank=True, null=True)
    prec = models.IntegerField(blank=True, null=True)
    recall = models.IntegerField(blank=True, null=True)
    f1 = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    epoch = models.IntegerField(blank=True, null=True)
    batchsize = models.IntegerField(blank=True, null=True)
    rnn_cell = models.CharField(max_length=20, blank=True, null=True)
    embedding = models.CharField(max_length=20, blank=True, null=True)
    bleu = models.FloatField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'role'


class RolePermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'role_permission'


class SimilarGraphs(models.Model):
    kgid = models.IntegerField(db_column='kgId')  # Field name made lowercase.
    similar_graphs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'similar_graphs'


class SysUser(models.Model):
    uid = models.BigAutoField(primary_key=True)
    login_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    type = models.IntegerField()
    state = models.TextField()  # This field type is a guess.
    email = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=50, blank=True, null=True)
    identityid = models.CharField(db_column='identityID', max_length=18)  # Field name made lowercase.
    birthday = models.CharField(max_length=10, blank=True, null=True)
    nation = models.CharField(max_length=50, blank=True, null=True)
    marriage = models.CharField(max_length=20, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    work_place = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class TaskResultEvaluationTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField(blank=True, null=True)
    model_id = models.BigIntegerField(blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    p_3 = models.CharField(db_column='p@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5 = models.CharField(db_column='p@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_3 = models.CharField(db_column='r@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_5 = models.CharField(db_column='r@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_3 = models.CharField(db_column='n@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_5 = models.CharField(db_column='n@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'task_result_evaluation_temp'


class TaskResultExplorationTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField(blank=True, null=True)
    model_id = models.BigIntegerField(blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    p_3 = models.CharField(db_column='p@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5 = models.CharField(db_column='p@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_3 = models.CharField(db_column='r@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_5 = models.CharField(db_column='r@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_3 = models.CharField(db_column='n@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_5 = models.CharField(db_column='n@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'task_result_exploration_temp'


class TaskResultSelectionTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField(blank=True, null=True)
    model_id = models.BigIntegerField(blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    p_3 = models.CharField(db_column='p@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5 = models.CharField(db_column='p@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_3 = models.CharField(db_column='r@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_5 = models.CharField(db_column='r@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_3 = models.CharField(db_column='n@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_5 = models.CharField(db_column='n@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'task_result_selection_temp'


class TaskResultTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField(blank=True, null=True)
    model_id = models.BigIntegerField(blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    p_3 = models.CharField(db_column='p@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5 = models.CharField(db_column='p@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_3 = models.CharField(db_column='r@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r_5 = models.CharField(db_column='r@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_3 = models.CharField(db_column='n@3', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_5 = models.CharField(db_column='n@5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'task_result_temp'


class UserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    role_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_role'

    def __str__(self):
        return 'user_id:'+str(self.user_id)+', role_id'+str(self.role_id)