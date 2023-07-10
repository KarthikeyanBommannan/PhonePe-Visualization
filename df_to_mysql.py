import mysql.connector as msc
from json_read_to_df import *

def main():
    def table1():
        conn = msc.connect(
                host = 'localhost',
                user ='root',
                password ='karthi123',
                port = '3306',
                db ='vikranthdb'
        )  
        if conn:
            print("Database connected successfully")
            agg_transaction_df = aggregate_transaction_by_state_all_year()

            try:
                database = conn.cursor()

                database.execute('DROP TABLE IF EXISTS agg_transaction CASCADE')

                database.execute('''CREATE TABLE IF NOT EXISTS agg_transaction (state VARCHAR(60),
                                                                        year INT8,
                                                                        quarter VARCHAR(10),
                                                                        transaction_type VARCHAR(80),
                                                                        transaction_count INT8,
                                                                        transaction_amount FLOAT8)''')

            # Prepare the INSERT statement with placeholders for the values
                insert_query1 = """
                        INSERT INTO agg_transaction (state,year,quarter,transaction_type,transaction_count,transaction_amount)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                
            # Iterate over each row in the DataFrame and execute the INSERT statement
                for _, row in agg_transaction_df.iterrows():
                    values = tuple(row)  # Convert the row to a tuple of values
                    database.execute(insert_query1, values)
            except Exception as e:
                print(f"The Error found is {str(e)}")
                
        conn.commit()
        print("Database disconnected successfully")
    table1()

    def table2():
        # state	year	quarter	brand_type	brand_count	brand_percentage
        conn = msc.connect(
                host = 'localhost',
                user ='root',
                password ='karthi123',
                port = '3306',
                db ='vikranthdb'
        )  
        if conn:
            print("Database connected successfully")
            agg_user_df = aggregate_user_by_state_all_year()

            try:
                database = conn.cursor()

                database.execute('DROP TABLE IF EXISTS agg_user CASCADE')

                database.execute('''CREATE TABLE IF NOT EXISTS agg_user (state VARCHAR(60),
                                                                        year INT8,
                                                                        quarter VARCHAR(10),
                                                                        brand_type VARCHAR(50),
                                                                        brand_count INT8,
                                                                        brand_percentage FLOAT8)''')

            # Prepare the INSERT statement with placeholders for the values
                insert_query2 = """
                        INSERT INTO agg_user (state,year,quarter,brand_type,brand_count,brand_percentage)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                
            # Iterate over each row in the DataFrame and execute the INSERT statement
                for _, row in agg_user_df.iterrows():
                    values = tuple(row)  # Convert the row to a tuple of values
                    database.execute(insert_query2, values)
            except Exception as e:
                print(f"The Error found is {str(e)}")
            
        conn.commit()
        print("Database disconnected successfully")
    table2()     
        
    def table3():
        # state	year	quarter	district	map_transaction_count	map_transaction_amount
        conn = msc.connect(
                host = 'localhost',
                user ='root',
                password ='karthi123',
                port = '3306',
                db ='vikranthdb'
        )  
        if conn:
            print("Database connected successfully")
            map_transaction_df = map_transaction_hover_by_state_all_year()

            try:
                database = conn.cursor()

                database.execute('DROP TABLE IF EXISTS map_transaction CASCADE')

                database.execute('''CREATE TABLE IF NOT EXISTS map_transaction (state VARCHAR(60),
                                                                        year INT8,
                                                                        quarter VARCHAR(10),
                                                                        district VARCHAR(50),
                                                                        map_transaction_count INT8,
                                                                        map_transaction_amount FLOAT8)''')

            # Prepare the INSERT statement with placeholders for the values
                insert_query3 = """
                        INSERT INTO map_transaction (state,year,quarter,district,map_transaction_count,map_transaction_amount)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                
            # Iterate over each row in the DataFrame and execute the INSERT statement
                for _, row in map_transaction_df.iterrows():
                    values = tuple(row)  # Convert the row to a tuple of values
                    database.execute(insert_query3, values)
            except Exception as e:
                print(f"The Error found is {str(e)}")
                
        conn.commit()
        print("Database disconnected successfully")
    table3()        
            
    def table4():
            # state	year	quarter	district	registered_users	app_opening
        conn = msc.connect(
                host = 'localhost',
                user ='root',
                password ='karthi123',
                port = '3306',
                db ='vikranthdb'
        )  
        if conn:
            print("Database connected successfully")
            map_user_df = map_user_hover_by_state_all_year()

            try:
                database = conn.cursor()

                database.execute('DROP TABLE IF EXISTS map_user CASCADE')

                database.execute('''CREATE TABLE IF NOT EXISTS map_user (state VARCHAR(60),
                                                                        year INT8,
                                                                        quarter VARCHAR(10),
                                                                        district VARCHAR(50),
                                                                        registered_users INT8,
                                                                        app_opening INT8)''')

            # Prepare the INSERT statement with placeholders for the values
                insert_query4 = """
                        INSERT INTO map_user (state,year,quarter,district,registered_users,app_opening)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                
            # Iterate over each row in the DataFrame and execute the INSERT statement
                for _, row in map_user_df.iterrows():
                    values = tuple(row)  # Convert the row to a tuple of values
                    database.execute(insert_query4, values)
            except Exception as e:
                print(f"The Error found is {str(e)}")
                
        conn.commit()
        print("Database disconnected successfully")
    table4()        
            
    def table5():
            # state	year	quarter	district	count	amount
            conn = msc.connect(
                    host = 'localhost',
                    user ='root',
                    password ='karthi123',
                    port = '3306',
                    db ='vikranthdb'
            )  
            if conn:
                print("Database connected successfully")
                top_transaction_df = top_transaction_state_all_year()

                try:
                    database = conn.cursor()

                    database.execute('DROP TABLE IF EXISTS top_transaction CASCADE')

                    database.execute('''CREATE TABLE IF NOT EXISTS top_transaction (state VARCHAR(60),
                                                                            year INT8,
                                                                            quarter VARCHAR(10),
                                                                            district VARCHAR(50),
                                                                            count INT8,
                                                                            amount FLOAT8)''')

                # Prepare the INSERT statement with placeholders for the values
                    insert_query5 = """
                            INSERT INTO top_transaction (state,year,quarter,district,count,amount)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """
                    
                # Iterate over each row in the DataFrame and execute the INSERT statement
                    for _, row in top_transaction_df.iterrows():
                        values = tuple(row)  # Convert the row to a tuple of values
                        database.execute(insert_query5, values)
                except Exception as e:
                    print(f"The Error found is {str(e)}")
                    
            conn.commit()
            print("Database disconnected successfully")
    table5()
        
    def table6():
        # state	year	quarter	district	registered_user
            conn = msc.connect(
                    host = 'localhost',
                    user ='root',
                    password ='karthi123',
                    port = '3306',
                    db ='vikranthdb'
            )  
            if conn:
                print("Database connected successfully")
                top_user_df = top_user_state_all_year()

                try:
                    database = conn.cursor()

                    database.execute('DROP TABLE IF EXISTS top_user CASCADE')

                    database.execute('''CREATE TABLE IF NOT EXISTS top_user (state VARCHAR(60),
                                                                            year INT8,
                                                                            quarter VARCHAR(10),
                                                                            district VARCHAR(50),
                                                                            registered_users INT8)''')

                # Prepare the INSERT statement with placeholders for the values
                    insert_query6 = """
                            INSERT INTO top_user (state,year,quarter,district,registered_users)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                    
                # Iterate over each row in the DataFrame and execute the INSERT statement
                    for _, row in top_user_df.iterrows():
                        values = tuple(row)  # Convert the row to a tuple of values
                        database.execute(insert_query6, values)
                except Exception as e:
                    print(f"The Error found is {str(e)}")
                    
            conn.commit()
            print("Database disconnected successfully")
    table6()     
        
    def table7():
        # state	pincode	year	quarter	total_transcation_count	total_transcation_amount
            conn = msc.connect(
                    host = 'localhost',
                    user ='root',
                    password ='karthi123',
                    port = '3306',
                    db ='vikranthdb'
            )  
            if conn:
                print("Database connected successfully")
                top_transpin_df = top_transaction_state_pincode()

                try:
                    database = conn.cursor()

                    database.execute('DROP TABLE IF EXISTS top_transpin CASCADE')

                    database.execute('''CREATE TABLE IF NOT EXISTS top_transpin (state VARCHAR(60),
                                                                            pincode INT8,
                                                                            year INT8,
                                                                            quarter VARCHAR(10),
                                                                            total_transaction_count INT8,
                                                                            total_transaction_amount INT8)''')

                # Prepare the INSERT statement with placeholders for the values
                    insert_query7 = """
                            INSERT INTO top_transpin (state,pincode,year,quarter,total_transaction_count,total_transaction_amount)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """
                    
                # Iterate over each row in the DataFrame and execute the INSERT statement
                    for _, row in top_transpin_df.iterrows():
                        values = tuple(row)  # Convert the row to a tuple of values
                        database.execute(insert_query7, values)
                except Exception as e:
                    print(f"The Error found is {str(e)}")
                    
            conn.commit()
            print("Database disconnected successfully")
    table7()     
        
    def table8():
        # state	pincode	year	quarter	registered_user
            conn = msc.connect(
                    host = 'localhost',
                    user ='root',
                    password ='karthi123',
                    port = '3306',
                    db ='vikranthdb'
            )  
            if conn:
                print("Database connected successfully")
                top_userpin_df = top_user_state_pincode()

                try:
                    database = conn.cursor()

                    database.execute('DROP TABLE IF EXISTS top_userpin CASCADE')

                    database.execute('''CREATE TABLE IF NOT EXISTS top_userpin (state VARCHAR(60),
                                                                            pincode INT8,
                                                                            year INT8,
                                                                            quarter VARCHAR(10),
                                                                            registered_users INT8)''')

                # Prepare the INSERT statement with placeholders for the values
                    insert_query8 = """
                            INSERT INTO top_userpin (state,pincode,year,quarter,registered_users)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                    
                # Iterate over each row in the DataFrame and execute the INSERT statement
                    for _, row in top_userpin_df.iterrows():
                        values = tuple(row)  # Convert the row to a tuple of values
                        database.execute(insert_query8, values)
                except Exception as e:
                    print(f"The Error found is {str(e)}")
                    
            conn.commit()
            print("Database disconnected successfully")
    table8()
    
if __name__ == "__main__":
    main()
    