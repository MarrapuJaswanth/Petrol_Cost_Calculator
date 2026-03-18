import streamlit as st

st.set_page_config(page_title="Jaswanth's Petrol Cost Calculator", page_icon="⛽")

st.title("⛽ Jaswanth's Petrol Cost Calculator")

# Sidebar choice
choice = st.sidebar.selectbox(
    "Choose Calculation Type",
    ["Monthly Petrol Cost", "Trip Petrol Cost"]
)

# ------------------ Monthly Petrol ------------------
if choice == "Monthly Petrol Cost":
    st.header("Monthly Petrol Cost Calculator")

    travel = st.number_input("Enter your one-side daily travel (km)", min_value=1)
    min_mileage = st.number_input("Enter minimum mileage (km/l)", min_value=1)
    max_mileage = st.number_input("Enter maximum mileage (km/l)", min_value=int(min_mileage))
    days = st.number_input("Enter working days per month", min_value=1)
    petrol_price = st.number_input("Enter petrol price (INR)", min_value=1.0)

    if st.button("Calculate Monthly Cost"):
        st.subheader("Results:")
        for mileage in range(int(min_mileage), int(max_mileage) + 1):
            cost = (((travel * 2) * days) / mileage) * petrol_price
            st.write(f"🚴 Mileage: {mileage} km/l")
            st.success(f"Monthly Petrol Cost: ₹ {cost:.2f}")
            st.write("---")

# ------------------ Trip Petrol ------------------
elif choice == "Trip Petrol Cost":
    st.header("Trip Petrol Cost Calculator")

    dist = st.number_input("Enter one-side trip distance (km)", min_value=1)
    min_mileage = st.number_input("Enter minimum mileage (km/l)", min_value=1, key="trip_min")
    max_mileage = st.number_input("Enter maximum mileage (km/l)", min_value=int(min_mileage), key="trip_max")
    petrol_price = st.number_input("Enter petrol price (INR)", min_value=1.0, value=107.46)

    if st.button("Calculate Trip Cost"):
        total_dist = dist * 2
        st.subheader("Results:")
        for mileage in range(int(min_mileage), int(max_mileage) + 1):
            total_petrol = total_dist / mileage
            cost = total_petrol * petrol_price
            st.write(f"🚴 Mileage: {mileage} km/l")
            st.success(f"Trip Petrol Cost: ₹ {cost:.2f}")
            st.write("---")
