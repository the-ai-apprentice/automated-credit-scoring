import streamlit as st
from visual_elements import apply_sidebar, apply_custom_css
from scoring_logic import predict_risk

st.set_page_config(
    page_title="Credit Risk Modelling Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

#initialize the state session variables
if "probability" not in st.session_state:
    st.session_state.probability = "--"
if "credit_score" not in st.session_state:
    st.session_state.credit_score = "--"
if "rating" not in st.session_state:
    st.session_state.rating = "Pending"

apply_sidebar(probability = st.session_state.probability,
              credit_score = st.session_state.credit_score,
              rating = st.session_state.rating)

# Main Area: Credit Risk Modeling
st.markdown(
    """
    <div>
        <h2 style="margin-bottom: 1px; font-weight: 600;">Credit Risk Modeling</h2>
        <div style="border-bottom: 1px solid #4a5057; margin-bottom: 25px;"></div>
        <p style="color: #A0AEC0; font-size: 13px; font-weight: 600; letter-spacing: 0.5px; margin-bottom: 15px;">CLIENT FINANCIAL PROFILE</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1_1, col2_1, col3_1 = st.columns(3)

with col1_1:
    age = st.number_input("**Age**",
                          min_value = 18,
                          max_value = 70,
                          value = 18,
                          step = 1)
    income = st.number_input("**Income**",
                             min_value = 1,
                             value = 1)

    loan_amount = st.number_input("**Loan Amount**",
                                  min_value = 0,
                                  value = 0)

with col2_1:
    delinquent_months = st.number_input("**Delinquent Months**",
                                        min_value = 0,
                                        max_value = 24)
    credit_util = st.number_input("**Credit Utilization Ratio**",
                                  min_value = 0,
                                  max_value = 100,
                                  value = 0)
    total_dpd = st.number_input("**Total DPD (Dates Past Due)**",
                                min_value = 0,
                                max_value = 180,
                                value = 0)

with col3_1:
    loan_tenure_months = st.number_input("**Loan Tenure (months)**",
                                         min_value = 6,
                                         value = 6)
    open_loan_accounts = st.number_input("**Open Loan Accounts**",
                                         min_value = 0,
                                         max_value = 5,
                                         value = 1)

st.markdown(
    '<div style="border-bottom: 1px solid #4a5057; margin-top: 25px; margin-bottom: 25px;"></div>',
    unsafe_allow_html=True
)

col1_2, col2_2, col3_2 = st.columns(3)

with col1_2:
    residence_type = st.selectbox("**Residence Type**",
                                  options = ['Owned', 'Mortgage', 'Rented'],
                                  index = 0)
with col2_2:
    loan_purpose = st.selectbox("**Loan Purpose**",
                                options = ['Home', 'Education', 'Personal', 'Auto'],
                                index = 0)
with col3_2:
    loan_type = st.selectbox("**Loan Type**",
                             options = ['Secured', 'Unsecured'],
                             index = 0)

input_dict = {
    "cust_id": ["C99999"],
    "age": [age],
    "gender": ["M"],
    "marital_status": ["Married"],
    "employment_status": ["Salaried"],
    "income": [income],
    "number_of_dependants": [2],
    "residence_type": [residence_type],
    "years_at_current_address": [5],
    "city": ["Mumbai"],
    "state": ["Maharashtra"],
    "zipcode": [400001],
    "loan_id": ["L99999"],
    "loan_purpose": [loan_purpose],
    "loan_type": [loan_type],
    "sanction_amount": [5000000],
    "loan_amount": [loan_amount],
    "processing_fee": [48000.0],  # Kept under the 3% business rule
    "gst": [8640],
    "net_disbursement": [4743360],
    "loan_tenure_months": [loan_tenure_months],
    "principal_outstanding": [4000000],
    "bank_balance_at_application": [250000],
    "disbursal_date": ["2026-09-01"],
    "installment_start_dt": ["2026-10-01"],
    "number_of_open_accounts": [open_loan_accounts],
    "number_of_closed_accounts": [1],
    "total_loan_months": [48],
    "delinquent_months": [delinquent_months],
    "total_dpd": [total_dpd],
    "enquiry_count": [1],
    "credit_utilization_ratio": [credit_util]
}

st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
_, btn_col, _ = st.columns([1, 1, 1])
with btn_col:
    calculate_btn = st.button("Calculate Risk")

if calculate_btn:
    default_probability, credit_score, rating = predict_risk(input_dict)
    st.session_state.probability = round(default_probability * 100, 2)
    st.session_state.credit_score = round(credit_score)
    st.session_state.rating = rating
    st.rerun()