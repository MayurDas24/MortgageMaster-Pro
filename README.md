🏠 MortgageMaster (Python)

A high-precision mortgage analysis suite built with Streamlit

MortgageMaster is a professional-grade mortgage calculation platform that generates accurate monthly payments, full amortization schedules, tax/insurance impacts, and exportable reports (CSV + PDF). Designed for financial clarity and built for real-world use cases.

🚀 Key Features
📌 1. Smart Mortgage Calculator

Computes:

Principal & Interest

Property tax (monthly)

Home insurance (monthly)

HOA fees

Accepts multiple currencies (₹, $, €, £, ¥)

Calculates down payment percentage instantly

Supports loan terms from 1 to 50 years

📊 2. Interactive Visual Insights

Beautiful Altair donut chart showing payment breakdown

Summary KPI metrics:

Loan Amount

Total Interest Paid

Total Cost of Loan

📉 3. Full Amortization Table

Month-by-month schedule including:

Principal Payment

Interest Payment

Cumulative Interest

Remaining Balance

Fully formatted and scrollable

Expandable UI element

📄 4. Export Options
CSV Export

1-click export of entire amortization schedule

PDF Export (Professional Report)

Auto-generated PDF with:

Title section

Summary table

Full amortization table

Styled using ReportLab

Professional formatting

Finance-ready deliverable for clients or documentation

💡 5. Modern UI / UX

Wide layout for maximum readability

Styled metric cards

Clean typography

Responsive layout across devices

Built-in section dividers & spacing

🧠 How the App Works
Mortgage Formula

Uses the industry-standard loan amortization formula:

Monthly Payment (P&I):

𝑀
=
𝑃
⋅
𝑟
(
1
+
𝑟
)
𝑛
(
1
+
𝑟
)
𝑛
−
1
M=P⋅
(1+r)
n
−1
r(1+r)
n
	​


Where:

P = Principal

r = Monthly interest rate

n = Number of payments

Amortization Loop

Each month, the model computes:

Interest due

Principal paid

Updated balance

Running total interest

PDF Generation Workflow

Creates a full PDF in memory using BytesIO

Styled tables with alternating colors

Exports on demand

📁 Project Structure
📂 MortgageMaster
│── app.py                     # Main Streamlit application
│── README.md                  # Documentation
│── requirements.txt            # Dependencies (recommended)

🔧 Installation & Setup
1. Clone the Repo
git clone <your-repo-url>
cd MortgageMaster

2. Install Dependencies
streamlit
pandas
numpy
altair
reportlab


Or via:

pip install -r requirements.txt

3. Run the App
streamlit run app.py

📤 Exported Outputs
Format	Contents	Purpose
CSV	Full amortization schedule	Excel/spreadsheet users
PDF Report	Summary + full schedule	Clients, documentation, printing
🖼 UI Overview

Clean header

Two-column layout (Inputs → Results)

Donut visualization

Expander-based schedule table

Footer with developer signature

🧑‍💻 Author

Varsh Vishwakarma
AI • ML • DL • Data Science • Cloud • Full-Stack ML Developer
