from backend.dao import train_model_dao


def get_all_models():
    report_pos = train_model_dao.get_all_models()
    ret = []
    for report_po in report_pos:
        if report_po.classification == "ArticleNet":
            continue
        ret.append(report_po.name)
    return ret