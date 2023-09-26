from backend.models import SimilarGraphs


def get_similar_graphs(kId: int):
    similar_graphs = list(SimilarGraphs.objects.filter(kgid=kId))
    return similar_graphs
