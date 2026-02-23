import streamlit as st

st.title("🧮 Simple Web Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate"):
    if operation == "Addition":
        result = a + b
    elif operation == "Subtraction":
        result = a - b
    elif operation == "Multiplication":
        result = a * b
    elif operation == "Division":
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"

    st.success(f"Result: {result}")