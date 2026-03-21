import streamlit as st
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Churn Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
}
.card {
    background: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
h1, h2, h3 {
    color: #1f2937;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Overview", "📈 Analysis", "🤖 Prediction", "🧠 Explainability", "🎯 Action Center"]
)

st.sidebar.markdown("---")
st.sidebar.info("AI Churn Dashboard 💡")

# ---------------- OVERVIEW ----------------
if page == "🏠 Overview":

    st.markdown("""
    <div class="card">
        <h1>🚀 Customer Retention Intelligence</h1>
        <p style='color:gray;'>Predict, analyze and reduce customer churn using AI insights.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("<div class='card'>👥 <b>7043</b><br>Customers</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>📉 <b>26%</b><br>Churn Rate</div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'>⚠️ <b>1200</b><br>High Risk</div>", unsafe_allow_html=True)
    col4.markdown("<div class='card'>💰 <b>₹2.5L</b><br>Revenue Loss</div>", unsafe_allow_html=True)

    st.markdown("### 📊 Churn Distribution")

    fig = px.pie(
        values=[70, 30],
        names=["Stay", "Churn"],
        hole=0.6
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- ANALYSIS ----------------
elif page == "📈 Analysis":

    st.title("📈 Churn Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h3>Churn by Contract</h3></div>", unsafe_allow_html=True)
        st.bar_chart([500, 300, 200])

    with col2:
        st.markdown("<div class='card'><h3>Churn by Tenure</h3></div>", unsafe_allow_html=True)
        st.line_chart([10, 20, 15, 30])

# ---------------- PREDICTION ----------------
elif page == "🤖 Prediction":

    st.title("🤖 AI Churn Prediction")

    col1, col2 = st.columns(2)

    with col1:
        tenure = st.slider("Tenure (Months)", 0, 72, 12)
        monthly = st.number_input("Monthly Charges", value=50.0)

    with col2:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    st.markdown("---")

    if st.button("🚀 Predict Churn"):

        # Dummy logic (replace with model later)
        prob = 0.78

        st.markdown(f"""
        <div class="card">
            <h2>Prediction Result</h2>
            <p>Churn Probability: <b>{prob*100:.2f}%</b></p>
        </div>
        """, unsafe_allow_html=True)

        if prob > 0.6:
            st.error("🔴 High Risk Customer")
            st.markdown("<div class='card'>💡 Offer discount or long-term plan</div>", unsafe_allow_html=True)
        else:
            st.success("🟢 Low Risk Customer")

# ---------------- EXPLAINABILITY ----------------
elif page == "🧠 Explainability":

    st.title("🧠 Model Explainability")

    st.markdown("<div class='card'><h3>Feature Importance</h3></div>", unsafe_allow_html=True)
    st.info("SHAP plot will be shown here")

    st.markdown("<div class='card'><h3>Detailed Impact</h3></div>", unsafe_allow_html=True)
    st.info("Beeswarm plot will be shown here")

# ---------------- ACTION CENTER ----------------
elif page == "🎯 Action Center":

    st.title("🎯 Retention Strategy")

    st.markdown("<div class='card'><h3>High Risk Customers</h3></div>", unsafe_allow_html=True)

    st.dataframe({
        "Customer": ["C101", "C205", "C309"],
        "Risk": ["High", "High", "Medium"],
        "Action": [
            "Offer 20% discount",
            "Upgrade plan",
            "Customer support call"
        ]
    })