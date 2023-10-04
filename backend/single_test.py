# import scispacy
import spacy
import en_ner_bc5cdr_md
import lstm_predict

def en_ner(text):
    nlp = en_ner_bc5cdr_md.load()
    doc = nlp(text)
    res = []
    for entity in doc.ents:
        res.append([str(entity), str(entity.label_)])
    print(res)
# return res

def zh_ner(text):
    ner = lstm_predict.LSTMNER()
    s = string.strip()

    return lstm_predict.concatRes(ner.predict(s))
