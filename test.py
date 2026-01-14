import pickle
import numpy as np

# Load the model
with open('best_chronic_kidney_diseasemodel.pkl', 'rb') as f:
    model = pickle.load(f)
print(type(model))

# Test with example input
example_input = np.array([
    48, 70, 1.015, 4, 0, 1, 1, 0, 0, 117, 56, 3.8, 111, 2.5, 11.2, 32, 6700, 3.9, 1, 0, 0, 0, 1, 1
]).reshape(1, -1)

prediction = model.predict(example_input)
print("Prediction:", "Chronic Kidney Disease" if prediction[0] == 1 else "No Chronic Kidney Disease")