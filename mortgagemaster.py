import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- PRE-FLIGHT CONFIG ---
st.set_page_config(page_title="MortgageMaster Pro", page_icon="🏠", layout="wide")

# --- ULTIMATE UI OVERRIDE (Hides Deploy, Menu, and Footer) ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Background & Font Fixes */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }

    /* Goated Metric Cards */
    .metric-container {
        background: linear-gradient(145deg, #161b22, #0d1117);
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    .metric-title {
        color: #8b949e;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #58a6ff;
        font-size: 26px;
        font-weight: 800;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# --- FINANCIAL LOGIC ---
def get_amortization(principal, rate, years, extra=0):
    monthly_rate = (rate / 100) / 12
    months = int(years * 12)
    
    if monthly_rate > 0:
        base_pmt = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    else:
        base_pmt = principal / months

    data = []
    balance = principal
    total_int = 0
    
    for i in range(1, months + 1):
        interest = balance * monthly_rate
        # Ensure we don't overpay the last balance
        principal_pmt = min(balance, (base_pmt - interest) + extra)
        balance -= principal_pmt
        total_int += interest
        
        data.append({
            "Month": i,
            "Payment": principal_pmt + interest,
            "Principal": principal_pmt,
            "Interest": interest,
            "Remaining Balance": max(0, balance),
            "Cumulative Interest": total_int
        })
        if balance <= 0: break
            
    return base_pmt, total_int, pd.DataFrame(data)

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.markdown("## ⚙️ Control Panel")
    curr = st.selectbox("Currency", ["$", "₹", "€", "£", "¥"])
    
    with st.expander("🏠 Asset Details", expanded=True):
        price = st.number_input("Home Price", value=350000, step=5000)
        down = st.number_input("Down Payment", value=70000, step=5000)
    
    with st.expander("📈 Loan Terms", expanded=True):
        term = st.slider("Term (Years)", 1, 30, 30)
        interest = st.number_input("Rate (%)", value=6.5, step=0.01, format="%.2f")
    
    st.markdown("### 🚀 Payment Accelerator")
    extra_pmt = st.number_input(f"Extra Monthly Principal ({curr})", value=0, step=100)

# --- PROCESSING ---
loan_amount = price - down
monthly_base, total_interest, df_sched = get_amortization(loan_amount, interest, term, extra_pmt)

# --- MAIN DASHBOARD ---
st.title("🏠 MortgageMaster Pro")
st.markdown("#### Interactive Financial Modeling for Smart Ownership")
st.write("")

# Custom Metric Row (Solves the white box / visibility issue)
c1, c2, c3, c4 = st.columns(4)

def card(column, label, value):
    column.markdown(f"""
        <div class="metric-container">
            <div class="metric-title">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

card(c1, "Monthly Payment", f"{curr}{monthly_base + extra_pmt:,.2f}")
card(c2, "Loan Amount", f"{curr}{loan_amount:,.0f}")
card(c3, "Total Interest", f"{curr}{total_interest:,.0f}")
card(c4, "Payoff Time", f"{len(df_sched)/12:.1f} Years")

st.write("")

# --- VISUALS ---
v1, v2 = st.columns([2, 1])

with v1:
    st.subheader("📉 Debt Reduction Timeline")
    chart = alt.Chart(df_sched).mark_area(
        line={'color':'#58a6ff'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='#58a6ff', offset=0),
                   alt.GradientStop(color='transparent', offset=1)],
            x1=1, x2=1, y1=1, y2=0
        )
    ).encode(
        x=alt.X('Month:Q', title="Months to Payoff"),
        y=alt.Y('Remaining Balance:Q', title="Principal Owed"),
        tooltip=['Month', 'Remaining Balance']
    ).properties(height=400)
    st.altair_chart(chart, use_container_width=True)

with v2:
    st.subheader("📊 Cost Breakdown")
    pie_data = pd.DataFrame({
        'Category': ['Principal', 'Interest'],
        'Value': [loan_amount, total_interest]
    })
    pie = alt.Chart(pie_data).mark_arc(innerRadius=70, cornerRadius=5).encode(
        theta="Value:Q",
        color=alt.Color("Category:N", scale=alt.Scale(range=['#58a6ff', '#238636'])),
        tooltip=['Category', 'Value']
    ).properties(height=400)
    st.altair_chart(pie, use_container_width=True)

# --- DATA TABLE (Fixed Error Version) ---
with st.expander("📋 Full Amortization Schedule"):
    # Using simple formatting to avoid Matplotlib dependency errors
    st.dataframe(
        df_sched.style.format({
            "Payment": "{:,.2f}",
            "Principal": "{:,.2f}",
            "Interest": "{:,.2f}",
            "Remaining Balance": "{:,.2f}",
            "Cumulative Interest": "{:,.2f}"
        }),
        use_container_width=True
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: #8b949e;'><b>{st.session_state.get('user_name', 'Mayur R Das')}</b> | MIT Manipal Computer Science</div>", 
    unsafe_allow_html=True
)