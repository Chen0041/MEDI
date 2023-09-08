# import spacy
# import en_ner_bc5cdr_md
import en_core_sci_md

# en_ner_bc5cdr_md和en_core_sci_md兼容spacy3.4.4
# en_core_web_sm要求更高版本的spacy
# en_ner_bc5cdr_md对应的训练数据集：https://huggingface.co/datasets/tner/bc5cdr,
# a resource for chemical disease relation extraction
# en_ner_bc5cdr_md和en_core_web_sm都识别不出entity

# text = """
# Myeloid derived suppressor cells (MDSC) are immature
# myeloid cells with immunosuppressive activity.
# They accumulate in tumor-bearing mice and humans
# with different types of cancer, including hepatocellular
# carcinoma (HCC).
# """

nlp = en_core_sci_md.load()
text = """
Are the kidneys hyper attenuated? | Yes
What is the air under the patient's left hemidiaphragm? | Stomach bubble
Is/Are there pulmonary consolidations? | No
"""
doc = nlp(text)

print(list(doc.sents))

print(doc.ents)