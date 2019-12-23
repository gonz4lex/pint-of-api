import requests
import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize


def get_user_data(username: str):
    url = f"https://api.github.com/users/{ username }"
    response = requests.get(url).json()

    return response

def load_data(data: dict):
    df = pd.DataFrame.from_records([data])

    return df

st.title('GitHub user data explorer')

user = st.text_input('Select a username:')

if user is not '':
    data_load_state = st.text("Getting data...")
    data = get_user_data(user)
    df = load_data(data)
    data_load_state.text('Getting data... done!')

st.subheader('Raw response')
st.write(data) if user is not '' else 'Please select a GitHub username'

st.subheader('Raw data')
st.write(df) if user is not '' else 'Please select a GitHub username'


import streamlit as st
import requests as rq

# @st.cache
# def get_user(user: str):
#     url = f'https://api.github.com/users/{user}'
#     response = rq.get(url)

#     return response


# def display_data(data: rq.Response, show: bool):
#     st.write('The status code of this response is: ', data.status_code)
#     st.write('Therefore the request was: ', data.ok)
    
#     if show:
#         st.subheader('Data retrieved: ')
#         st.write(data.json())

# st.title('Github user explorator')

# user = st.text_input('Please choose a Github username:')

# if user:
#     data = get_user(user)


# show = st.checkbox('Show data?')

# display_data(data, show)
