from flask import Flask, request, jsonify, render_template
import numpy as np
from catboost import CatBoostClassifier

app = Flask(__name__)

# Load CatBoost model
model = CatBoostClassifier()
model.load_model("models/model.cbm")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"], dtype=float).reshape(1, -1)

        print("Received features:", features)
        print("Feature count:", features.shape[1])

        prediction = model.predict(features)

        result = (
            "Patient has Chronic Kidney Disease"
            if int(prediction[0]) == 1
            else "Patient does not have Chronic Kidney Disease"
        )

        return jsonify({"prediction": result})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
