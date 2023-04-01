import datetime
import streamlit as st
import pandas as pd
import numpy as np

#read dataset from csv file
df = pd.read_csv('data/airlines_delay.csv')
df = df.dropna()

#save min and max value of the column "Length" in variables
min_value_num = int(df['Length'].min())
max_value_num = int(df['Length'].max())

#create a slider to select the length of the column "Length"
length= st.slider("Length", min_value=min_value_num, max_value=max_value_num, value=max_value_num, step=1)
#create checkboxes for Yes and No and set both to false
yes = st.checkbox('Yes', value=False)
no = st.checkbox('No', value=False)

st.write("Length: ", length)
#show dataset in a table
edited_df = df[df['Length'] < length]
#rename column of df class to delayed
edited_df = edited_df.rename(columns={'Class': 'Delayed'})
#rename elements of column Delayed to Yes and No instead of 1 and 0
edited_df['Delayed'] = edited_df['Delayed'].replace({1: 'Yes', 0: 'No'})
#if yes is checked, show only rows with Delayed = Yes and if no is checked, show only rows with Delayed = No
if yes:
    edited_df = edited_df[edited_df['Delayed'] == 'Yes']
if no:
    edited_df = edited_df[edited_df['Delayed'] == 'No']

st.write(edited_df)


@st.cache
def fetch_and_clean_data(url):
# Fetch data from URL here, and then clean it up.
    return None

if 'date' not in st.session_state:
    st.session_state.date = datetime.datetime.now()

#show current datetime
st.write("App launched: ", st.session_state.date)

del st.session_state.date

