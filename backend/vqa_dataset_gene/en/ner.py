# use scispaCy for medical ner
# en_ner_bc5cdr_md和en_core_sci_md兼容spacy3.4.4
# en_core_web_sm要求更高版本的spacy
# en_ner_bc5cdr_md对应的训练数据集：https://huggingface.co/datasets/tner/bc5cdr, chemical disease relation extraction
# en_ner_bc5cdr_md和en_core_web_sm都识别不出entity，因此改为en_core_sci_md

# 测试模型是否正常：
# text = """
# Myeloid derived suppressor cells (MDSC) are immature
# myeloid cells with immunosuppressive activity.
# They accumulate in tumor-bearing mice and humans
# with different types of cancer, including hepatocellular
# carcinoma (HCC).
# """

import en_ner_bc5cdr_md
# import spacy
# import en_core_sci_md


def ner(text):
    nlp = en_ner_bc5cdr_md.load()
    # nlp = en_core_sci_md.load()
    doc = nlp(str(text))
    # print(doc.ents)
    res = []
    for entity in doc.ents:
        res.append([str(entity), str(entity.label_)])
    print(res)
    return res


