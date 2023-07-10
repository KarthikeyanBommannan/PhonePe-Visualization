import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import pygwalker as pgw

st.set_page_config(
    page_title="Tableau",
    layout="wide"
)

def load_data(data):
    return pd.read_csv(data)

def main():
    st.sidebar.form("Upload Form")
    data_file = st.sidebar.file_uploader("Upload CSV or XLXS File",type = ['csv','xlxs'])
    submittted = st.sidebar.button("Submit")
    if submittted:
        df = load_data(data_file)
        # st.dataframe(df)
        pgw_html = pgw.walk(df,return_html=True)
        stc.html(pgw_html,scrolling=True,height=700,width=1000)
        
        
if __name__ == "__main__":
    main()