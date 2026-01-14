import pandas as pd
from catboost import CatBoostClassifier

# Load dataset
data = pd.read_csv("data/kidney_disease.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Encode target
data["classification"] = data["classification"].replace(
    {"ckd": 1, "ckd\t": 1, "notckd": 0}
)

# Convert all features to numeric
data = data.apply(pd.to_numeric, errors="coerce")

# Fill missing values
data = data.fillna(data.median())

# Split features and target
X = data.drop(["classification", "id"], axis=1)
y = data["classification"]

# ⚠️ Handle class imbalance
class_weights = {
    0: 2.5,   # NOT-CKD (increase importance)
    1: 1.0    # CKD
}

# Train model
model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    loss_function="Logloss",
    class_weights=class_weights,
    verbose=False
)

model.fit(X, y)

# Save model
model.save_model("model.cbm")

print("✅ Model trained and saved as model.cbm")
