import streamlit as st
import re
import random

def handle_message(msg_content):
    if re.match(r"^rp[\d+\-]+$", msg_content):
        expression = msg_content[2:]

        if re.match(r"^[\d+\-]+$", expression):
            try:
                num = eval(expression)
                num = max(0, min(100, num))

                arr = []
                ones_placed = 0
                toggle = True

                for _ in range(100):
                    if toggle and ones_placed < num:
                        arr.append(1)
                        ones_placed += 1
                    else:
                        arr.append(0)
                    toggle = not toggle

                for i in range(100):
                    if ones_placed >= num:
                        break
                    if arr[i] == 0:
                        arr[i] = 1
                        ones_placed += 1

                result = random.choice(arr)
                return 'Yes' if result == 1 else 'No'

            except Exception as e:
                return f"Error: {str(e)}"

    return "Error: Invalid input format."


# Streamlit UI
st.title("Beyond the Shattered Horizon")
st.write("\n\n")

st.image('pic-1.png')
st.write("\n")

if 'history' not in st.session_state:
    st.session_state.history = [] 

# Input User
msg = st.text_input("Enter the Percentage", placeholder="rp50")

# Click Button
if st.button("Show Percentage"):
    if msg:
        response = handle_message(msg)
        st.session_state.history.append(response)
        st.write(response)
    else:
        st.write("Please Enter the Percentage.")

if st.session_state.history:
    st.write("\n### History of Previous Results:")
    for i, entry in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {entry}")