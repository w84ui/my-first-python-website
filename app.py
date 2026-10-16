import streamlit as st

st.title("My Python Web Experiment 🚀")
st.write("Welcome to my first website, built entirely in Python!")

# Add an interactive widget
name = st.text_input("What is your name?")
if name:
    st.success(f"Hello {name}! You just triggered web interactivity using Python code!")
else:
    print("Please enter your name!")
# Add a fun metric tracker
ambition_level = st.slider("How far do you want to push this website?", 0, 100, 50)
st.metric(label="Ambition Level", value=f"{ambition_level}%")
