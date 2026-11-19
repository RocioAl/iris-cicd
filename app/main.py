from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas import IrisInput

app = FastAPI(title="Iris Species Predictor API - CI/CD")

MODEL_PATH = Path("models/champion.joblib")
model = joblib.load(MODEL_PATH)

templates = Jinja2Templates(directory="templates")

SPECIES_MAP = {
    0: "Iris setosa",
    1: "Iris versicolor",
    2: "Iris virginica",
}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(flower: IrisInput):
    data = pd.DataFrame([flower.model_dump()])
    prediction = int(model.predict(data)[0])
    probabilities = model.predict_proba(data)[0]
    confidence = float(probabilities[prediction])

    if confidence < 0.60:
        confidence_level = "Bajo"
    elif confidence < 0.85:
        confidence_level = "Medio"
    else:
        confidence_level = "Alto"

    return {
        "prediction": prediction,
        "species": SPECIES_MAP[prediction],
        "confidence": round(confidence, 4),
        "confidence_level": confidence_level,
        "probabilities": {
            "setosa": round(float(probabilities[0]), 4),
            "versicolor": round(float(probabilities[1]), 4),
            "virginica": round(float(probabilities[2]), 4),
        },
        "message": f"Especie predicha: {SPECIES_MAP[prediction]} (Nivel de confianza: {confidence_level})",
    }
