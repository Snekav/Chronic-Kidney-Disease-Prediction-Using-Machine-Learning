from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model("models/model.cbm")

print("Model loaded successfully!")
