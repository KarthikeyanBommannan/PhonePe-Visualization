import streamlit as st
import pandas as pd
import plotly.express as px



selectbox_column, empty_column, map_column = st.columns([55,4,85])


with selectbox_column:
    
    # st.write("<style>div.row-widget.stButton > button {color: white !important;}</style>", unsafe_allow_html=True)

    # st.button('All India', disabled=True)
    col1, col2 = st.columns([8, 6])

    with col1:
        options = st.sidebar.selectbox("options", ('Transactions', 'Users'), key="options", label_visibility='collapsed')

    with col2:
        year = st.sidebar.selectbox("year", range(2018, 2023), key="year", label_visibility='collapsed')
        
    col3, col4 = st.columns([9, 7])

    with col3:
        quater = st.sidebar.selectbox("quater", ('Q1', 'Q2', 'Q3', 'Q4'), key='quater', label_visibility='collapsed')
        
with map_column:
    
    transactions = pd.read_csv(r"C:\Users\karthikeyan\OneDrive\Desktop\project2\geo_transactions.csv")
    users = pd.read_csv(r"C:\Users\karthikeyan\OneDrive\Desktop\project2\geo_users.csv")
    
    filtered_transactions = transactions[(transactions['Year'] == year) & (transactions['Quarter'] == quater)]
    filtered_users = users[(users['Year'] == year) & (users['Quarter'] == quater)]
    
    
    if options == 'Transactions':
        if year == year:
            if quater == quater:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                transactions['State'] = transactions['State'].str.replace('and ', '& ')
                transactions['State'] = transactions['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = px.choropleth_mapbox(data_frame=filtered_transactions,
                      geojson=geojson_file,
                      featureidkey='properties.ST_NM',
                      locations='State',
                      mapbox_style="carto-positron",
                      hover_data={'Transaction_count': ':,', 'Transaction_amount': ':,'},
                      color='State',
                      zoom=3,
                      color_continuous_scale=px.colors.colorbrewer.Set2,
                      )
                figure.update_geos(fitbounds = "geojson",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=800, height=800)
                figure.update_layout(
                        geo=dict(bgcolor='rgba(0,0,0,0)'),
                        plot_bgcolor='rgba(0,0,0,0)', 
                        )
                        
                st.plotly_chart(figure, use_container_width=True)
                
    if options == 'Users':
        if year == year:
            if quater == quater:
                
                geojson_file = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                
                users['State'] = users['State'].str.replace('and ', '& ')
                users['State'] = users['State'].str.replace('Andaman & Nicobar Islands', 'Andaman & Nicobar')
                
                figure = px.choropleth_mapbox(
        data_frame=filtered_users,
        geojson=geojson_file,
        featureidkey='properties.ST_NM',
        locations='State',
        mapbox_style="carto-positron",
        hover_data={'Registered_user': ':,', 'App_opening': ':,'},
        color='State',
        color_continuous_scale=px.colors.colorbrewer.Set2,
        zoom=3,
        center={"lat": 20.5937, "lon": 78.9629}
    )
                figure.update_geos(fitbounds = "geojson",visible=False)
                figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
                figure.update_layout(width=800, height=800)
                figure.update_layout(
                        geo=dict(bgcolor='rgba(0,0,0,0)'),
                        plot_bgcolor='rgba(0,0,0,0)', 
                        )
                        
                st.plotly_chart(figure, use_container_width=True)