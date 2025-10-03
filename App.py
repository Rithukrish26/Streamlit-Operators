import streamlit as st
st.title("Streamlit - Learning Project 1")
st.write("Hello, this is my first website using Streamlit.")
st.subheader("This is a webapp made for basic operations")
num1 = st.number_input("Enter a number:- ", value= 0)
num2 = st.number_input("Enter the other number:- ", value= 0)
# if st.button("add"):
#     a = num1 + num2
#     st.write(f"The sum of {num1} and {num2} is {a}")
# operator = st.text_input("Please enter the sign of the desired operator")
# if operator == "+":
#     if st.button("add"):
#         a = num1 + num2
#         st.write(f"The sum of {num1} and {num2} is {a}")
operator = st.selectbox("Choose the desired operator", ["+","-","*","/"])
if st.button("Calculate"):
    if operator == "+":
        a = num1 + num2
        st.write(f"The sum of {num1} and {num2} is {a}")

    if operator == "-":
        a = num1 - num2
        st.write(f"The difference between {num1} and {num2} is {a}")

    if operator == "*":
        a = num1 * num2
        st.write(f"The product of {num1} and {num2} is {a}")

    if operator == "/":
        a = num1 / num2

        st.write(f"The quotient of {num1} and {num2} is {a}")
