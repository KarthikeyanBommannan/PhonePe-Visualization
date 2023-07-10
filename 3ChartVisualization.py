import mysql.connector as msc
import pandas as pd
import streamlit as st
import plotly.express as px

conn = msc.connect(
    host='localhost',
    user='root',
    password='karthi123',
    port='3306',
    db='vikranthdb'
)

if conn:
    print("Database connected successfully")

def question1(year, quarter):
    database = conn.cursor()
    database.execute("SELECT transaction_type, SUM(transaction_amount) AS total_amount FROM agg_transaction WHERE year = %s AND quarter = %s GROUP BY transaction_type ORDER BY total_amount", (year, quarter))
    result1 = database.fetchall()
    output1 = pd.DataFrame(result1, columns=['transaction_type', 'transaction_amount']).reset_index(drop=True)
    output1.index += 1
    fig = px.bar(output1, x='transaction_type', y='transaction_amount', color='transaction_amount', 
                 color_continuous_scale='Spectral', hover_data=["transaction_type", "transaction_amount"], 
                 height=420, width=700)
    return fig

def question2(year, quarter):
    database = conn.cursor()
    database.execute("SELECT state, brand_type, SUM(brand_count) AS brand_count FROM agg_user WHERE year = %s AND quarter = %s GROUP BY state, brand_type ORDER BY brand_count DESC", (year, quarter))
    result2 = database.fetchall()
    output2 = pd.DataFrame(result2, columns=['State', 'Brand Type', 'Brand Count']).reset_index(drop=True)
    output2.index += 1
    fig2 = px.pie(output2, values='Brand Count', names='Brand Type', title='Brand Type Distribution')
    fig2.update_layout(width=600, height=450)
    fig2.update_traces(rotation=90)
    fig2.update_traces(hole=0.4)
    
    return fig2

def question3(year, quarter):
    database = conn.cursor()
    database.execute("SELECT district,sum(map_transaction_amount) FROM map_transaction WHERE year = %s and quarter = %s GROUP BY district ORDER BY sum(map_transaction_amount) DESC,district ASC LIMIT 10 ;", (year, quarter))
    result3 = database.fetchall()
    output3 = pd.DataFrame(result3, columns=['District', 'Transaction Amount']).reset_index(drop=True)
    output3.index += 1
    fig3 = px.bar(output3, x='District', y='Transaction Amount', color='Transaction Amount', 
                 color_continuous_scale='Spectral', hover_data=['District','Transaction Amount'], 
                 height=420, width=700)
    return fig3

def question4(year, quarter):
    database = conn.cursor()
    database.execute("SELECT state, district, SUM(registered_users) AS total_registered_users, SUM(app_opening) AS total_app_opening FROM map_user WHERE year = %s AND quarter = %s GROUP BY state, district ORDER BY total_registered_users DESC; ", (year, quarter))
    result4 = database.fetchall()
    output4 = pd.DataFrame(result4, columns=['State', 'District', 'Registered User', 'App Opening']).reset_index(drop=True)
    output4.index += 1
    fig4 = px.sunburst(output4, path=['State', 'District'], values='Registered User', color='Registered User', 
                   color_continuous_scale='darkmint', hover_data=['State', 'District', 'Registered User', 'App Opening'], 
                   height=750, width=750)
    return fig4

def question5(year, quarter):
    database = conn.cursor()
    database.execute("SELECT state,district,SUM(count) FROM top_transaction WHERE year = %s AND quarter = %s GROUP BY state,district ORDER BY SUM(count) DESC ;", (year, quarter))
    result5 = database.fetchall()
    output5 = pd.DataFrame(result5, columns=['State','District','Transaction Count']).reset_index(drop=True)
    output5.index += 1
    fig5 = px.bar(output5, x='State', y='Transaction Count', color='District', 
                 color_continuous_scale='Spectral', hover_data=['State','District','Transaction Count',], 
                 height=700, width=1000)
    
    return fig5

def question6(year, quarter):
    database = conn.cursor()
    database.execute("SELECT state, pincode, SUM(total_transaction_count), SUM(total_transaction_amount) FROM top_transpin WHERE year = %s and quarter = %s GROUP BY state, pincode ORDER BY SUM(total_transaction_amount) DESC LIMIT 10;", (year, quarter))
    result6 = database.fetchall()
    output6 = pd.DataFrame(result6, columns=['State', 'Pincode', 'Transaction Count', 'Transaction Amount']).reset_index(drop=True)
    output6.index += 1
    fig6 = px.density_heatmap(output6, x='State', y='Transaction Count', z='Pincode', color_continuous_scale='Purp_r',
                          height=700, width=800)

    return fig6




year = st.sidebar.selectbox("Select the Year",(2018,2019,2020,2021,2022))
quarter = st.sidebar.selectbox("Slect the Quarter",('Q1','Q2','Q3','Q4')) 
questions = st.sidebar.selectbox("Select One Question Below",("Tap to view",
                                                              "1.what are the Transaction Type and its Transaction Amount ",
                                                              "2.what are the Top 10 Brand Type and its usage count",
                                                              "3.what are the Top 10 District wise Transaction",
                                                              "4.what are the Registered users and App Opening with respect to states",
                                                              "5.what are the Transaction Count by State",
                                                              "6.what are the Top 10 Top Transaction by Pincode"))


if questions == "1.what are the Transaction Type and its Transaction Amount ":
        figs = question1(year,quarter)
        st.write(f"The Result is for the {year} and {quarter}")
        st.plotly_chart(figs)

if questions == "2.what are the Top 10 Brand Type and its usage count":
        figs = question2(year,quarter)
        st.write(f"The Result is for the {year} and {quarter}")
        st.plotly_chart(figs)

if questions == "3.what are the Top 10 District wise Transaction":
        figs = question3(year,quarter)
        st.write(f"The Result is for the {year} and {quarter}")
        st.plotly_chart(figs)

if questions == "4.what are the Registered users and App Opening with respect to states":
        figs = question4(year,quarter)
        st.write(f"The Result is for the {year} and {quarter}")
        st.plotly_chart(figs)
        
if questions == "5.what are the Transaction Count by State":
        figs = question5(year,quarter)
        st.write(f"The Result is for the {year}")
        st.plotly_chart(figs)

if questions == "6.what are the Top 10 Top Transaction by Pincode":
        figs = question6(year,quarter)
        st.write(f"The Result is for the {year}")
        st.plotly_chart(figs)
