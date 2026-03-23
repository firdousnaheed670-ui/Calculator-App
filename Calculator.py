import streamlit as st

st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Perform calculation when button is clicked
if st.button("Calculate"):
    if operation == "Add":
        st.success(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "Subtract":
        st.success(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "Multiply":
        st.success(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "Divide":
        if num2 != 0:
            st.success(f"{num1} / {num2} = {num1 / num2}")
        else:
            st.error("Error! Division by zero.")
