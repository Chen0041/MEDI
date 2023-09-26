from backend.dao import similar_cases_dao


def get_similar_graphs(kdId):
    similar_cases = similar_cases_dao.get_similar_cases(kdId)
    if len(similar_cases) == 0:
        result = ''
        # call python
        return result
    else:
        return similar_cases[0]