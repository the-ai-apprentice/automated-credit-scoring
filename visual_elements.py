import streamlit as st


def apply_custom_css():
    custom_css = """
    <style>
/* Main app background */
.stApp {
    background-color: #fbfbf9; /* Light off-white matching mockup */
    color: #1e2638;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Fix extra white space at the top */
[data-testid="stHeader"] {
    background-color: transparent !important;
}
.block-container {
    padding-top: 2rem !important; 
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #e6e5df !important; /* Light beige/grey sidebar to match mockup */
    border-right: 1px solid #d1d4dc !important;
}

/* Headers and text */
h1, h2, h3, p, label {
    color: #1a202c !important;
}

h2 {
    font-weight: 600 !important;
    letter-spacing: 0.5px;
}

/* 1. Input fields and Select boxes - Base Backgrounds */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stNumberInputContainer"],
div[data-testid="stTextInput"] > div > div {
    background-color: #ffffff !important; 
    border: 1px solid #cbd5e1 !important; 
    border-radius: 4px !important;
}

/* 2. Strip background from nested divs */
div[data-testid="stNumberInputContainer"] > div,
div[data-testid="stNumberInputContainer"] > div > div,
div[data-baseweb="select"] > div > div,
div[data-baseweb="select"] > div > div > div {
    background-color: transparent !important;
}

/* 3. Force Text Color */
input[type="number"], 
input[type="text"],
div[data-baseweb="select"] *,
div[data-baseweb="select"] span {
    color: #1e293b !important;
    -webkit-text-fill-color: #1e293b !important;
    font-size: 14px !important;
}

/* 4. Dropdown caret (arrow) icon color */
div[data-baseweb="select"] svg {
    fill: #64748b !important;
    color: #64748b !important;
}

/* 5. The Popover Dropdown Menu */
div[data-baseweb="popover"] ul,
ul[data-testid="stSelectboxVirtualDropdown"],
ul[role="listbox"] {
    background-color: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
}

/* 6. The individual options in the dropdown */
li[role="option"] {
    background-color: transparent !important;
    color: #1e293b !important;
}

/* 7. Hover effect for options */
li[role="option"]:hover,
li[aria-selected="true"] {
    background-color: #f1f5f9 !important;
}

/* Horizontal separator */
hr {
    border-color: #e2e8f0;
}

/* Hide the +/- stepper buttons */
div[data-testid="stNumberInputContainer"] button {
    display: none !important; 
}

/* Button styling (UPDATE ANALYSIS) */
.stButton > button {
    background-color: #528bb8 !important; /* Lighter blue */
    color: white !important;
    border: none;
    border-radius: 4px;
    padding: 0.6rem 2.5rem;
    font-weight: bold !important; /* Changed from 600 to bold */
    letter-spacing: 0.5px;
    display: block;
    margin: 1.6rem auto; /* Keeps the button shifted up */
}

/* Force white and bold text on the button AND its inner text tags */
.stButton > button, 
.stButton > button p, 
.stButton > button div {
    color: #ffffff !important;
    font-weight: bold !important;
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    background-color: #3b6b91 !important; /* Uses your old button color for the hover state */
    color: white !important;
}

/* Ensure text stays white on hover */
.stButton > button:hover, 
.stButton > button:hover p, 
.stButton > button:hover div {
    color: #ffffff !important;
}

/* Analysis Results Stat Cards - Main Area */
[data-testid="stMetric"] {
    background-color: #ffffff !important; 
    padding: 2px 15px;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05); 
}

/* Center metric values and labels */
[data-testid="stMetricValue"] {
    font-size: 1.5rem;
    font-weight: 500;
    display: flex;
    justify-content: center;
    padding-top: 10px;
}
[data-testid="stMetricLabel"] {
    display: flex;
    justify-content: center;
    color: #1e293b !important;
    font-size: 1.5rem;
    font-weight: 500;
}

/* Target individual Metric Colors based on column order */
/* Default Probability */
[data-testid="column"]:nth-child(1) [data-testid="stMetricValue"] {
    color: #c0392b !important; 
}
/* Credit Score */
[data-testid="column"]:nth-child(2) [data-testid="stMetricValue"] {
    color: #2980b9 !important; 
}
/* Rating */
[data-testid="column"]:nth-child(3) [data-testid="stMetricValue"] {
    color: #27ae60 !important; 
}

/* Hide the expand control and collapse button */
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarCollapseButton"] { display: none !important; }

/* Sidebar Selectbox Label tweaks */
[data-testid="stSidebar"] label p {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: #475569 !important;
}

/* Force Selectbox backgrounds to white */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
}

/* Reduce font size inside the selectbox dropdowns */
[data-testid="stSidebar"] div[data-baseweb="select"] {
    font-size: 13px !important;
}

/* Reduce the vertical spacing between widgets in the sidebar */
[data-testid="stSidebar"] .stElementContainer {
    margin-bottom: -8px !important;
}

[data-testid="stSidebarUserContent"] {
    padding-bottom: 0rem !important;
}

/* Reduce vertical gaps between rows of input fields in the main area */
div[data-testid="stVerticalBlock"] {
    gap: 0.75rem !important; /* Streamlit's default is usually larger; adjust this to 0.5rem if you want it even tighter */
}

/* Slightly reduce the invisible padding around individual input widgets */
.stElementContainer {
    margin-bottom: -5px !important; 
}

</style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def apply_sidebar(probability = "--", credit_score = "--", rating = "Pending"):
    with st.sidebar:
        st.markdown("""
            <div style="margin-bottom: 25px;">
                <p style="font-size: 28px; font-weight: 700; margin: 0;">LAUKI Finance</p>
                <p style="font-size: 18px; font-weight: 600; margin: 0; padding-top: 2px;">Risk Analytics</p>
            </div>
            """,
                    unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<p style="color: #A0AEC0; font-size: 13px; font-weight: 600; letter-spacing: 0.5px;">PROJECT DETAILS & CONFIG</p>',
            unsafe_allow_html=True
        )

        dataset_version = st.selectbox(
            "**Dataset Version:**",
            options=["v02.24"],
            index=0,
            disabled=True
        )
        st.markdown("<br>", unsafe_allow_html=True)

        model_type = st.selectbox(
            "**Model Type:**",
            options=["Logistic Regression v2"],
            index=0,
            disabled=True
        )
        st.markdown(
            '<div style="border-bottom: 1px solid #4a5057; margin-top: 20px; margin-bottom: 20px;"></div>',
            unsafe_allow_html=True
        )

        # Analysis Results Section Header
        st.markdown(
            '<p style="color: #A0AEC0; font-size: 13px; font-weight: 600; letter-spacing: 0.5px;">ANALYSIS RESULTS</p>',
            unsafe_allow_html=True
        )

        st.metric(label = "Default Probability", value = f"{probability} %")
        st.metric(label = "Credit Score", value = f"{credit_score}")
        st.metric(label = "Rating", value = f"{rating}")
