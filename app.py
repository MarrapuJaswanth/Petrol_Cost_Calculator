import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Petrol Cost Calculator",
    page_icon="⛽",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
        }
        .stApp {
            background: linear-gradient(to right, #0f172a, #1e293b);
            color: white;
        }
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #1e293b;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("⛽ Petrol Cost Dashboard")
st.caption("Smart way to estimate your fuel expenses")

# ---------- Sidebar ----------
choice = st.sidebar.radio(
    "Select Calculation",
    ["Monthly Cost", "Trip Cost"]
)

# ---------- Monthly ----------
if choice == "Monthly Cost":
    st.markdown("## 📅 Monthly Petrol Cost")

    col1, col2 = st.columns(2)

    with col1:
        travel = st.number_input("One-side daily travel (km)", min_value=1)
        days = st.number_input("Working days/month", min_value=1)

    with col2:
        min_mileage = st.number_input("Min mileage (km/l)", min_value=1)
        max_mileage = st.number_input("Max mileage (km/l)", min_value=int(min_mileage))
        petrol_price = st.number_input("Petrol price (₹)", value=107.0)

    if st.button("Calculate 🚀"):
        data = []
        for mileage in range(int(min_mileage), int(max_mileage) + 1):
            cost = (((travel * 2) * days) / mileage) * petrol_price
            data.append({"Mileage": mileage, "Cost": cost})

        df = pd.DataFrame(data)

        # ---------- Metrics ----------
        st.markdown("### 💡 Summary")
        col1, col2, col3 = st.columns(3)

        col1.metric("Min Cost", f"₹ {df['Cost'].min():.2f}")
        col2.metric("Max Cost", f"₹ {df['Cost'].max():.2f}")
        col3.metric("Avg Cost", f"₹ {df['Cost'].mean():.2f}")

        # ---------- Chart ----------
        st.markdown("### 📊 Cost vs Mileage")
        st.line_chart(df.set_index("Mileage"))

        # ---------- Table ----------
        with st.expander("📋 Detailed Breakdown"):
            st.dataframe(df, use_container_width=True)

# ---------- Trip ----------
elif choice == "Trip Cost":
    st.markdown("## 🛣️ Trip Petrol Cost")

    col1, col2 = st.columns(2)

    with col1:
        dist = st.number_input("One-side distance (km)", min_value=1)

    with col2:
        min_mileage = st.number_input("Min mileage (km/l)", min_value=1, key="t1")
        max_mileage = st.number_input("Max mileage (km/l)", min_value=int(min_mileage), key="t2")
        petrol_price = st.number_input("Petrol price (₹)", value=107.0, key="t3")

    if st.button("Calculate Trip 🚀"):
        total_dist = dist * 2
        data = []

        for mileage in range(int(min_mileage), int(max_mileage) + 1):
            petrol = total_dist / mileage
            cost = petrol * petrol_price
            data.append({"Mileage": mileage, "Cost": cost})

        df = pd.DataFrame(data)

        # ---------- Metrics ----------
        st.markdown("### 💡 Summary")
        col1, col2, col3 = st.columns(3)

        col1.metric("Min Cost", f"₹ {df['Cost'].min():.2f}")
        col2.metric("Max Cost", f"₹ {df['Cost'].max():.2f}")
        col3.metric("Avg Cost", f"₹ {df['Cost'].mean():.2f}")

        # ---------- Chart ----------
        st.markdown("### 📊 Cost vs Mileage")
        st.line_chart(df.set_index("Mileage"))

        # ---------- Table ----------
        with st.expander("📋 Detailed Breakdown"):
            st.dataframe(df, use_container_width=True)

# ---------- Footer ----------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
