# LAUKI Finance: Credit Risk Analytics Dashboard

> An automated, machine learning-driven credit risk evaluation dashboard designed to eliminate operational bottlenecks and instantly assess default probabilities for loan applications.

## 📖 Project Overview

**Lauki Finance** previously faced significant operational bottlenecks due to the manual evaluation of credit scores and loan applications. This time-consuming process severely limited the number of customers the company could efficiently serve.

To address this, we developed an automated **Machine Learning Credit Risk Model and Scoring System**. This interactive Streamlit dashboard allows loan officers to input client financial profiles and instantly receive actionable risk analytics, including:

* 🎯 **Default Probability (%)**
* 📈 **Dynamic Credit Score (300 - 900)**
* 🚦 **Risk Rating (Poor, Average, Good, Excellent)**

## ✨ Key Features

* 🖥️ **Interactive User Interface:** A clean, visually appealing dashboard built with Streamlit and customized CSS.
* ⚡ **Instant Risk Analytics:** Real-time generation of credit scores and default probabilities based on user inputs.
* ⚙️ **Robust Feature Engineering:** Calculates critical risk indicators under the hood, such as:
  * *Loan-to-Income Ratio (LTI)*
  * *Delinquency Ratio*
  * *Average Days Past Due (DPD) per Delinquency*
* 🔍 **Highly Explainable ML:** Powered by a fine-tuned Logistic Regression model, ensuring regulatory compliance and transparent decision-making.

## 🧠 Machine Learning Workflow

The underlying predictive model was rigorously trained and evaluated to meet strict business requirements (>90% recall for catching defaults, >50% precision).

1. 🧹 **Data Preprocessing & EDA:** Handled business-logic anomalies (e.g., impossible processing fees) and dropped features with high multicollinearity using Variance Inflation Factor (VIF).
2. 🎯 **Feature Selection:** Utilized Weight of Evidence (WOE) and Information Value (IV) to select only the most predictive features.
3. ⚖️ **Class Imbalance:** Applied **SMOTE-Tomek** to synthesize minority class data and remove noisy links, successfully resolving the severe imbalance in default records.
4. 🤖 **Model Selection & Tuning:** Used `Optuna` to optimize both XGBoost and Logistic Regression. **Logistic Regression** was selected as the final model due to its high explainability, achieving a **0.98 ROC AUC**, a **0.967 Gini Coefficient**, and a **94% Recall** for predicting defaulters.

## 🛠️️ Technology Stack

* **Frontend:** Streamlit 🌐
* **Data Processing:** Pandas, NumPy 📊
* **Machine Learning:** Scikit-Learn, Imbalanced-Learn (SMOTE-Tomek), Optuna, XGBoost 🧠
* **Model Serialization:** Joblib 💾

## 📂 Project Structure

```text
automated-credit-scoring/
├── artifacts/
│   └── risk_model_data.joblib             # Serialized ML model, scaler, and encoder
├── notebook/
│   └── Credit_Risk_Modelling.ipynb        # EDA, SMOTE-Tomek balancing, and Optuna tuning
├── main.py                                # Main Streamlit application and layout
├── requirements.txt                       # Python dependencies
├── scoring_logic.py                       # Input preprocessing and prediction logic
└── visual_elements.py                     # Custom CSS and Streamlit UI configurations
```

## 🚀 Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/automated-credit-scoring.git
cd automated-credit-scoring
```

### 2️⃣ Install dependencies

Ensure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

Start the Streamlit server:

```bash
streamlit run main.py
```

### 4️⃣ Interact

Open your browser to `http://localhost:8501`. Enter the client's financial and demographic details into the input fields and click **"Calculate Risk"** to view their resulting credit rating and default probability.
