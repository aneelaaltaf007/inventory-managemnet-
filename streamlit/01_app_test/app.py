import streamlit as st

# Adding the function of your app
st.title('My first App')

# Adding simple text
st.write('Here is a simple text')

# user input
number = st.slider('Pick a number', 0, 100)

# Adding the text of number
st.write(f'You selected: { number}')

