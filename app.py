import pickle
import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing import normalize_corpus

class stackoverflow_question(BaseModel):
    Title: str
    Body: str

app = FastAPI()

# Charge le pipeline sklearn (TF-IDF + MultiOutputClassifier avec Reg Log)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Charge la liste des classes (venant du MultiLabelBinarizer)
with open("classes.pkl", "rb") as f:
    classes = pickle.load(f)


@app.post('/proba')
def get_proba(data: stackoverflow_question):

    received = data.dict()

    concat_inputs = received["Title"] + " " + received["Body"]

    normalized_inputs = normalize_corpus(concat_inputs)

    pred_proba = model.predict_proba([normalized_inputs])

    zip_proba = zip(
        classes, 
        np.vstack(pred_proba)[:,1]
        )

    proba = dict(zip_proba)

    return proba


#@app.post('/prediction')
#def get_prediction(data: SO_post):



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)