import argparse
import json
import os
import zipfile
import csv
import shutil

from backend.models import CtInformation
from .PreProcess import removePrivacy
from .lstm_predict import predictAll

def organizeOriginalData(src_path):
    with open(src_path + '/relationship.csv', 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        img_txt_dic = {}
        for row in reader:
            print(row)
            if row[0] == 'txtid':
                continue
            img_txt_dic[row[1]] = row[0]

        print(img_txt_dic)
        if not os.path.exists(src_path + '/organizedData'):
            os.mkdir(src_path + '/organizedData')

        for key, value in img_txt_dic.items():
            source_img_path = src_path + '/img/' + key + '.jpg'
            source_txt_path = src_path + '/txt/' + value + '.txt'
            new_dir_path = src_path + '/organizedData/' + key
            os.mkdir(new_dir_path)
            target_img_path = new_dir_path + '/' + key + '.jpg'
            target_txt_path = new_dir_path + '/' + value + '.txt'

            shutil.copy(source_img_path, target_img_path)
            shutil.copy(source_txt_path, target_txt_path)

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

def generateQuestions(dicname):
    for i in os.listdir(dicname):
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.jpg':
            imgname = dicname +'/'+ i
        elif os.path.splitext(i)[1] == '.txt':
            textname = dicname +'/'+ i

    textPreProcessedName = dicname + '/preprocessed.txt'

    NERinputName = textPreProcessedName
    NERoutputName = dicname + '/entity.json'

    dialist=predictAll(NERinputName,  NERoutputName)
    text = removePrivacy(textname, textPreProcessedName)
    # need fix
    patient_id = textname.split('/')[-1]
    photo_id = imgname.split('/')[-1]
    annotation = ''
    dataset = "xx"
    ct_info = CtInformation(patient_id=patient_id, sym=text, photo_id=photo_id, dia_list=dialist, annotation=annotation, status='0', dataset=dataset)
    ct_info.save()

    QApath = dicname + '/QA.txt'

    os.remove(textPreProcessedName)

    with open(NERoutputName, 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        for data in json_data.values():
            print(data)
            i = 0
            while (i != len(data)):
                if len(data[i]) == 1:
                    data.pop(i)
                    i = i - 1
                i = i + 1
            data = list(set(data))
            print(data)
        QA = generateDISnCHECK(json_data["DISEASE"], json_data["CHECK"])
        print(QA)
        with open(QApath, 'w', encoding='utf8') as f:
            for i in QA:
                f.write(i + '\n')
    # os.remove(resultEntity)


# input : resultEntity
# output : questions
def generateDISnCHECK(dis,check):
    dis=','.join(dis)
    check=','.join(check)

    question='我有'+dis+',可以进行什么检查？'
    answer='可以考虑'+check
    return [question,answer]


def copyImgToImgpath(zip_dest, imgDest):
    imgSrcPath = zip_dest + '/img'
    if not os.path.exists(imgDest + '/' + zip_dest.split('/')[-1]):
        print(imgDest)
        print(zip_dest.split('/')[-1])
        os.mkdir(imgDest + '/' + zip_dest.split('/')[-1])
    for i in os.listdir(imgSrcPath):
        src = imgSrcPath + '/' + i

        dest = imgDest + '/' + zip_dest.split('/')[-1] + '/' + i
        shutil.copy(src, dest)


def main(src, imgpath):

    zipDest=src[:-4]
    unzip_file(src, zipDest)
    organizeOriginalData(zipDest)
    copyImgToImgpath(zipDest, imgpath)

    for dic in os.listdir(zipDest+"/organizedData"):
        dicname = zipDest+"/organizedData" + '/' + dic
        print(os.listdir(dicname))
        generateQuestions(dicname)


# main(src)
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--name', default='test')
#     args = parser.parse_args()
#     dataset = args.name
#     print(dataset)
#     main(dataset)

