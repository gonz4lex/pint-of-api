import streamlit as st
import requests as rq

@st.cache
def get_user(user: str):
    url = f'https://api.github.com/users/{user}'
    response = rq.get(url)

    return response


def display_data(data: rq.Response, show: bool):
    st.write('The status code of this response is: ', data.status_code)
    st.write('Therefore the request was: ', data.ok)
    
    if show:
        st.subheader('Data retrieved: ')
        st.write(data.json())

st.title('Github user explorator')

user = st.text_input('Please choose a Github username:')

if user:
    data = get_user(user)


show = st.checkbox('Show data?')

display_data(data, show)
