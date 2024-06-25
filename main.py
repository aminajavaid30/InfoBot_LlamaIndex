import streamlit as st
from infobot_llamaindex import get_response

st.title("InfoBot - Your AI Assistant")
st.subheader("LlamaIndex")

query = st.text_input("Ask InfoBot a question:")

if st.button("Submit"):
    if query:
        response = get_response(query)
        st.write(response.response)
    else:
        st.write("Please enter a question.")
