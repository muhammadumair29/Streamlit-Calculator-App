import streamlit as st

# App title
st.title("🧮 Simple Streamlit Calculator")

# Input fields
st.header("Enter two numbers:")
num1 = st.number_input("First Number", step=1.0, format="%.2f")
num2 = st.number_input("Second Number", step=1.0, format="%.2f")

# Select operation
operation = st.selectbox("Choose Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed!")
