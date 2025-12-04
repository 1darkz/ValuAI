# ValuAI
A complete end-to-end machine learning project that predicts house sale prices using structured data.  
Includes data cleaning, exploratory analysis, feature engineering, model training, evaluation, and explainability.

---

## 🎯 Project Goal
Predict the **SalePrice** of houses based on property characteristics such as:
- CRIM: per capita crime rate by town
- ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
- INDUS: proportion of non-retail business acres per town
- CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- NOX: nitric oxides concentration (parts per 10 million)
- RM: average number of rooms per dwelling
- AGE: proportion of owner-occupied units built prior to 1940
- DIS: weighted distances to five Boston employment centres
- RAD: index of accessibility to radial highways
- TAX: full-value property-tax rate per $10,000
- PTRATIO: pupil-teacher ratio by town
- B: The result of the equation B=1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- LSTAT: % lower status of the population

This project uses modern ML techniques and emphasizes interpretability and clean engineering practices.

---

## ✔️ Key Features

### **1. Data Cleaning and preprocessing**
- Handle missing values
- Remove duplicates
- Convert categorical variables to numeric
- Feature scaling

### **2. Exploratory Data Analysis (EDA)**
- Visualize data distributions
- Identify correlations
- Detect outliers

### **3. Feature Engineering**
- Transform existing features
- Handle missing values

### **4. Model Training**
Trained and compared:
- Linear Regression  
- Lasso / Ridge  
- Random Forest  
- XGBoost  
- CatBoost  
- Hyperparameter tuning with RandomizedSearch / Optuna 

### **5. Model Evaluation**
Metrics Included:
- R2
- RMSE
- Residual analysis
- Training vs validation performance

### **6. Model Explainability**
Using **SHAP values**:
- Top contributing features  
- Individual prediction explanations  
- Summary plots 

---

## 🚀 How to run

### **1. Install dependencies**

```bash
pip install -r requirements.txt
```

### **2. Run EDA**
Open:
notebooks/01_eda.ipynb

### **3. Train model**
Run:
notebooks/02_modeling.ipynb
or programmatically:
python src/train.py

### **4. Evaluate model**
python src/evaluate.py


---

## 📈 Results Summary
- Best Model: CatBoost Regressor
- Achieved R2: 0.76
- Achieved MSE: 4.04
- Most important features:
    - RM
    - AGE
    - LSTAT

---

### 🛠 Technologies Used
- Python
- Pandas / Numpy
- Scikit-learn
- XGBoost
- CatBoost
- Matplotlib / Seaborn
- SHAP
- Jupyter Notebook

### 📌 Future Improvements
- Deploy model with Streamlit or FastAPI
- Add prediction intervals
- Implement automated ML pipelines with MLflow
- Improve hyperparameter optimization with Optuna

--- 

### 📄 Dataset
This project uses the Boston House Prices-Advanced Regression Techniques dataset from Kaggle.

Dataset is not included in the repo due to licensing.

---

### 🤝 Contributions
Contributions are welcome! Please open an issue or submit a pull request.

---

### 📧 Contact 
If you want help improving this project or turning it into a portfolio piece, feel free to reach out.

---

### 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.