from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
import os

from django.views.decorators.csrf import csrf_exempt

from backend.vqa_dataset_gene.zh.main import generateQuestions

@csrf_exempt
def test(request):
    zipDest = 'C:/Users/CZS/Desktop/IDEA_Project/MEDI/VQAdataset/Slake'
    for dic in os.listdir(zipDest+"/organizedData"):
        dicname = zipDest+"/organizedData" + '/' + dic
        generateQuestions(dicname)
    return HttpResponse("succeed")
