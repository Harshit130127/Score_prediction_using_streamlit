#  Student Exam Score Prediction

This project was completed as part of my Data Science Internship at **Celebal Technologies**. The goal was to build a machine learning model to predict a student’s academic exam score based on various input features. This was the **main project** of the internship and involved end-to-end data science workflow — from preprocessing and analysis to model deployment.

---

##  Problem Statement

To develop a predictive model that estimates a student's exam score based on:

- Hours Studied  
- Previous Exam Scores  
- Extracurricular Activities  
- Sleep Hours  
- Sample Question Papers Practiced

---

## Steps Performed

### 1. **Data Preprocessing**
- Handled missing values
- Label encoded categorical data
- Feature scaling applied where necessary

### 2. **Exploratory Data Analysis (EDA)**
- Visualized distributions and relationships
- Identified correlations using heatmaps
- Detected and handled outliers

### 3. **Model Training**
Evaluated various regression models including:
- Linear Regression
- Ridge & Lasso Regression
- Decision Tree & Random Forest
- Gradient Boosting & AdaBoost
- Support Vector Regressor
- XGBoost

Each model was assessed using R², RMSE, and MAE to determine performance.

### 4. **Model Selection**
The model with the **best R² score** was selected and saved for deployment.

### 5. **Deployment with Streamlit**
Developed a simple Streamlit app where users can input student details and get real-time score predictions.

---

## Project Files

- `student_exam_score_prediction.ipynb` – Notebook with complete EDA and model workflow  
- `Student_Performance.csv` – Dataset used  
- `best_model.pkl` – Trained model for prediction  
- `app.py` – Streamlit-based frontend interface  
- `README.md` – Project overview and documentation

---

##  Key Learnings

- Applied end-to-end machine learning pipeline in a real-world scenario  
- Improved understanding of multiple regression techniques  
- Hands-on experience with model evaluation, comparison, and deployment  
- Built an interactive UI for model usage using Streamlit

---

##  Conclusion

This project helped me bridge the gap between theory and practice. It was the **main highlight** of my internship and allowed me to apply everything I learned through structured weekly assignments. Excited to take these skills further into future real-world challenges.

---


