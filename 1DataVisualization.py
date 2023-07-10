import mysql.connector as msc
import pandas as pd
import streamlit as st
st.set_page_config(page_title = "Data Visualization",page_icon = "U+1F4C4")
conn = msc.connect(
                host = 'localhost',
                user ='root',
                password ='karthi123',
                port = '3306',
                db ='vikranthdb'
        )  

if conn:
        print("Database connected successfully")
        
def consolidated_transaction_output(year,quarter):
	
        
                database = conn.cursor()
                st.write(":green[Transactions]")
                st.write("All PhonePe transactions (UPI + Cards + Wallets)")
                database.execute("SELECT SUM(transaction_count) AS count FROM agg_transaction WHERE year = %s AND quarter = %s", (year, quarter))
                result1 = database.fetchall()
                output1 = pd.DataFrame(result1,columns = ['All PhonePe transactions (UPI + Cards + Wallets)']).reset_index(drop=True)
                output1.index+=1
                st.text(output1.to_string(index=False))
                
                col1,col2 = st.columns(2)
                col1.write(":white[Total Payment Values]")
                database.execute("SELECT SUM(transaction_amount) FROM agg_transaction WHERE year = %s AND quarter = %s", (year, quarter))
                result2 = database.fetchall()
                output2 = pd.DataFrame(result2,columns = ['Total payment value']).reset_index(drop=True)
                output2.index+=1
                col1.text(output2.to_string(index=False))
                
                col2.write(":white[Avg. transaction value]")
                database.execute("SELECT AVG(transaction_amount/transaction_count) AS amount FROM agg_transaction WHERE year = %s AND quarter = %s", (year, quarter))
                result3 = database.fetchall()
                output3 = pd.DataFrame(result3,columns = ['Avg.transaction value']).reset_index(drop=True)
                output3.index+=1
                col2.text(output3.to_string(index=False))
               
                st.write(":white[Categories]")
                database.execute("SELECT transaction_type,SUM(transaction_count) FROM agg_transaction WHERE year = %s AND quarter = %s GROUP BY transaction_type", (year, quarter))
                result4 =database.fetchall()
                output4 = pd.DataFrame(result4,columns =['categories','transaction_amount'])
                output4.index+=1
                st.text(output4.to_string(index=False))
               
                col3,col4,col5 = st.columns(3)
                database.execute("SELECT state ,SUM(transaction_count) AS count FROM agg_transaction WHERE year = %s AND quarter = %s GROUP BY state ORDER BY SUM(transaction_count) DESC LIMIT 10", (year, quarter))
                result5 = database.fetchall()
                output5 = pd.DataFrame(result5,columns = ['states','amount']).reset_index(drop=True)
                output5.index+=1
                col3.text(output5.to_string(index=False))
                
                database.execute("SELECT district,SUM(count) FROM top_transaction WHERE year = %s AND quarter = %s GROUP BY district ORDER BY SUM(count) DESC LIMIT 10", (year, quarter))
                result6 = database.fetchall()
                output6 = pd.DataFrame(result6,columns = ['district','amount']).reset_index(drop=True)
                output6.index+=1
                col4.text(output6.to_string(index=False))
                
                database.execute("SELECT pincode,SUM(total_transaction_count) FROM top_transpin WHERE year = %s AND quarter = %s GROUP BY pincode ORDER BY SUM(total_transaction_count) DESC LIMIT 10", (year, quarter))
                result7 = database.fetchall()
                output7 = pd.DataFrame(result7,columns = ['pincode','amounts']).reset_index(drop=True)
                output7.index+=1
                col5.text(output6.to_string(index=False))
                    
                    
def consolidated_user_output(year,quarter):
                database = conn.cursor()
                st.write(":green[Users]")
                st.write("Registered PhonePe users till Q1 2018")
                database.execute("SELECT SUM(registered_users) AS total FROM map_user WHERE year = %s AND quarter = %s", (year, quarter))
                result1 = database.fetchall()
                output1 = pd.DataFrame(result1,columns = ['Registered PhonePe users till Q1 2018']).reset_index(drop=True)
                output1.index+=1
                st.text(output1.to_string(index=False))
                
                st.write(":white[PhonePe app opens in Q1 2018]")
                database.execute("SELECT SUM(app_opening) FROM map_user WHERE year = %s AND quarter = %s", (year, quarter))
                result2 = database.fetchall()
                output2 = pd.DataFrame(result2,columns = ['app_opening']).reset_index(drop=True)
                output2.index+=1
                st.text(output2.to_string(index=False))
                
                col3,col4,col5 = st.columns(3)
                database.execute("SELECT state,SUM(registered_users) FROM map_user WHERE year = %s AND quarter = %s GROUP BY state ORDER BY SUM(registered_users) DESC LIMIT 10", (year, quarter))
                result3 = database.fetchall()
                output3 = pd.DataFrame(result3,columns = ['state','registered_users']).reset_index(drop=True)
                output3.index+=1
                col3.text(output3.to_string(index=False))
                
                
                database.execute("SELECT district,SUM(registered_users) FROM top_user WHERE year = %s AND quarter = %s GROUP BY district ORDER BY SUM(registered_users) DESC LIMIT 10", (year, quarter))
                result4 =database.fetchall()
                output4 = pd.DataFrame(result4,columns =['district','registered_users'])
                output4.index+=1
                col4.text(output4.to_string(index=False))
                
                
                database.execute("SELECT pincode,SUM(registered_users) FROM top_userpin WHERE year = %s AND quarter = %s GROUP BY pincode ORDER BY SUM(registered_users) DESC LIMIT 10", (year, quarter))
                result5 = database.fetchall()
                output5 = pd.DataFrame(result5,columns = ['pincode','registered_users']).reset_index(drop=True)
                output5.index+=1
                col5.text(output5.to_string(index=False))
    


options = st.sidebar.selectbox('Select One Options',('Transactions','Users'))  
year = st.sidebar.selectbox("Select the Year",(2018,2019,2020,2021,2022))
quarter = st.sidebar.selectbox("Slect the Quarter",('Q1','Q2','Q3','Q4')) 
if options == "Transactions":
	if year == year:
		if quarter == quarter:
			consolidated_transaction_output(year,quarter)

elif options == "Users":
	if year == year:
		if quarter == quarter:
			consolidated_user_output(year,quarter)