"""VitalCare — health-insurance cost estimation demo."""
from pathlib import Path
import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "insurance_model.pkl"
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

try:
    model = joblib.load(MODEL_PATH)
except Exception as exc:
    model = None
    MODEL_LOAD_ERROR = str(exc)
else:
    MODEL_LOAD_ERROR = None

REGIONS = {"northwest", "southeast", "southwest", "northeast"}

def make_features(data):
    age = int(data.get("age", ""))
    bmi = float(data.get("bmi", ""))
    children = int(data.get("children", ""))
    sex = data.get("sex", "female").lower()
    smoker = data.get("smoker", "no").lower()
    region = data.get("region", "northeast").lower()
    if not 18 <= age <= 100:
        raise ValueError("Please enter an age between 18 and 100.")
    if not 10 <= bmi <= 80:
        raise ValueError("Please enter a BMI between 10 and 80.")
    if not 0 <= children <= 10:
        raise ValueError("Please enter a number of children between 0 and 10.")
    if sex not in {"female", "male"}:
        raise ValueError("Please choose a valid sex option.")
    if smoker not in {"yes", "no"}:
        raise ValueError("Please choose a valid smoking status.")
    if region not in REGIONS:
        raise ValueError("Please choose a valid region.")
    # Feature order must match the supplied trained model.
    return np.array([[age, bmi, children, int(sex == "male"), int(smoker == "yes"),
                      int(region == "northwest"), int(region == "southeast"),
                      int(region == "southwest")]], dtype=float)

def estimate(data):
    if model is None:
        raise RuntimeError("The prediction model could not be loaded. Please check the model file and dependencies.")
    features = make_features(data)
    value = float(model.predict(features)[0])
    return max(0.0, value)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    try:
        cost = estimate(request.form)
        return render_template("index.html", prediction=cost, submitted=request.form)
    except (ValueError, TypeError) as exc:
        return render_template("index.html", error=str(exc), submitted=request.form), 400
    except RuntimeError as exc:
        app.logger.exception("Model is unavailable")
        return render_template("index.html", error=str(exc), submitted=request.form), 503

@app.post("/api/predict")
def api_predict():
    data = request.get_json(silent=True) or {}
    try:
        return jsonify({"estimated_annual_cost": round(estimate(data), 2), "currency": "USD", "disclaimer": "An educational estimate, not a quote or medical advice."})
    except (ValueError, TypeError) as exc:
        return jsonify({"error": str(exc)}), 400
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 503

@app.get("/health")
def health():
    return jsonify({"status": "ok" if model is not None else "degraded", "model_loaded": model is not None}), (200 if model is not None else 503)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
