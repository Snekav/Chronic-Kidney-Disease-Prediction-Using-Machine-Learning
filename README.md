
# Chronic Kidney Disease Prediction 🩺

## 📌 Project Overview

This project focuses on building a machine learning model to predict Chronic Kidney Disease (CKD) using patient clinical and lab data. Early detection can help initiate timely treatment and reduce long-term health complications.

## 🎯 Objective

Develop an accurate classification model to predict whether a patient is likely to have CKD based on features like:

Blood pressure

Blood glucose

Serum creatinine

Hemoglobin

Other lab and clinical features.

---

## 📊 Dataset

- **Source**: UCI Machine Learning Repository  
- **Filename**: `kidney_disease.csv`  
- **Total Samples**: 400  
- **Features**: 24 input features + 1 target  
- **Target Variable**: `class` (values: `ckd`, `notckd`)

---

## 🧰 Technologies Used

- **Language**: Python  
- **Libraries**:
  - Data Handling: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `catboost`, `lightgbm`
  - Flask:  `web deployment`

---

## 🔍 Project Workflow

### 1. Data Cleaning
- Dropped unnecessary columns
- Renamed features for clarity
- Handled missing values (mode & random sampling)
- Converted categorical data to numerical
- Standardized inconsistent entries

### 2. Exploratory Data Analysis (EDA)
- Plotted feature distributions
- Identified correlations and trends
- Visualized missing values and outliers

### 3. Feature Engineering
- Label-encoded categorical variables
- Performed train-test split (70/30)

### 4. Model Building
Trained and compared multiple models:
- Decision Tree
- Random Forest
- Gradient Boosting
- Extra Trees
- CatBoost
- LightGBM
- **CatBoost Classifier** (selected as final model based on accuracy)

### 5. Hyperparameter Tuning
- Used `GridSearchCV` to optimize Decision Tree

### 6. Evaluation
Metrics used:
- Accuracy
- Confusion Matrix
- Precision, Recall, F1-score

---

## 📈 Model Accuracy Comparison

| # | Classifier                   | Score(Decimal)    | Score (%) |
| - | ---------------------------- | -------- | --------- |
| 1 | Gradient Boosting Classifier | 0.977000 | 97.7%     |
| 2 | CatBoost                     | 1.000000 | 100%      |
| 3 | Stochastic Gradient Boosting | 0.991667 | 99.17%    |
| 4 | Decision Tree Classifier     | 0.983333 | 98.33%    |
| 5 | Random Forest Classifier     | 0.975000 | 97.5%     |
| **CatBoost**                                | **100%**     |

✅**CatBoost Classifier** achieved the highest accuracy and was selected as the final model.

**Why CatBoost?** It handles categorical variables efficiently without manual encoding and reduces overfitting, making it highly suitable for structured tabular data like CKD features.


---

## 🏃‍♂️ How to Run the Project

### 1. Clone the repository:
   
   git clone https://github.com/yourusername/ckd-prediction.git
   cd ckd-prediction
   
### 2.Install required libraries:


  pip install -r requirements.txt

### 3.Run the Flask app:

python app.py

 ### 4.Open browser

 http://127.0.0.1:5000/

 ### Enter patient details and click Predict


## 👤 Sample Patient Prediction


ckd_patient_data = {
    'age': 55,
    'blood_pressure': 140,
    'specific_gravity': 1.030,
    'albumin': 2,
    'sugar': 0,
    'red_blood_cells': 1,
    'pus_cell': 2,
    'pus_cell_clumps': 1,
    'bacteria': 1,
    'blood_glucose_random': 95,
    'blood_urea': 80,
    'serum_creatinine': 2.5,
    'sodium': 135,
    'potassium': 5.2,
    'hemo': 11.5,
    'packed_cell_volume': 37,
    'white_blood_cell_count': 9500,
    'red_blood_cell_count': 4.8,
    'hypertension': 1,
    'diabetes_mellitus': 0,
    'coronary_artery_disease': 0,
    'appetite': 0,
    'pedal_edema': 1,
    'anemia': 1
}
### View prediction


 ## Screenshots


![FEATIURES1](https://github.com/user-attachments/assets/7194ef55-ca93-45bd-944c-68436f79b367)



![OP1](https://github.com/user-attachments/assets/3e1706fe-94f4-438f-84ee-4634b2124d7f)
![OP1](https://github.com/user-attachments/assets/d605d799-f84b-4e71-af9b-6262ddc33f35)
![OP1](https://github.com/user-attachments/assets/2008a007-5963-4ea0-a171-eba5cd858ada)
![OP1](https://github.com/user-attachments/assets/b7671b3c-c1e0-4524-9eb7-87ecbb057d43)


##  🏁 Conclusion
This project enables prediction of Chronic Kidney Disease (CKD) using machine learning.

- Data cleaned and preprocessed for accurate predictions

- Multiple models tested; CatBoost gave the best results

- Tool can assist doctors in early detection and treatment of CKD
 ### Key Points:

 - We cleaned and prepared the data to ensure accurate predictions.

 - Multiple models were tested, and CatBoost   gave the best results.

- This tool can assist doctors in early detection and treatment of CKD.
=======
# Chronic-Kidney-Disease-Prediction-Using-Machine-Learning
This project focuses on building a machine learning model to predict Chronic Kidney Disease (CKD) using patient clinical and laboratory data. Early detection of CKD can help initiate timely treatment and reduce long-term health complications.

