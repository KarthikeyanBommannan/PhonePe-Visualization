import os
import json
import pandas as pd

# Aggregated TRANSACTION by STATE
def aggregate_transaction_by_state_all_year():
    PATH = "D:/Phonepe/data/aggregated/transaction/country/india/state/"
    statelist = os.listdir(PATH)
    aggregate_transaction_dict = {
        'state': [],
        'year': [],
        'quarter': [],
        'transaction_type': [],
        'transaction_count': [],
        'transaction_amount': []
    }

    for i in statelist:
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)

        for j in state_year_list:
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)

            for k in statewise_year_files:
                jFile = statewise_year_file_list + k
                data = open(jFile, "r")
                output = json.load(data)
                try:
                    for transaction_data in output['data']['transactionData']:
                        name = transaction_data['name']
                        count = transaction_data['paymentInstruments'][0]['count']
                        amount = transaction_data['paymentInstruments'][0]['amount']
                        aggregate_transaction_dict['transaction_type'].append(name.replace('-',' ').lower())
                        aggregate_transaction_dict['transaction_count'].append(count)
                        aggregate_transaction_dict['transaction_amount'].append(amount)
                        aggregate_transaction_dict['state'].append(i.replace('-',' '))
                        aggregate_transaction_dict['year'].append(j)
                        aggregate_transaction_dict['quarter'].append('Q' + k.strip('.json'))
                except Exception as e:
                    pass
    aggregate_df = pd.DataFrame(aggregate_transaction_dict)
    return aggregate_df




# Aggregated USER by STATE
def aggregate_user_by_state_all_year():
    PATH = "D:/Phonepe/data/aggregated/user/country/india/state/"
    statelist = os.listdir(PATH)
    aggregate_transaction_dict = {
        'state': [],
        'year': [],
        'quarter': [],
        'brand_type': [],
        'brand_count': [],
        'brand_percentage': []
    }

    for i in statelist:
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)
        
        for j in state_year_list:
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files:
                jsFile = statewise_year_file_list + k
                data1 = open(jsFile, "r")
                output1 = json.load(data1)
                try:
                    for transaction_data in output1['data']['usersByDevice']:
                        brand = transaction_data['brand']
                        count = transaction_data['count']
                        percentage = transaction_data['percentage']
                        aggregate_transaction_dict['brand_type'].append(brand.lower())
                        aggregate_transaction_dict['brand_count'].append(count)
                        aggregate_transaction_dict['brand_percentage'].append(percentage)
                        aggregate_transaction_dict['state'].append(i.replace('-',' '))
                        aggregate_transaction_dict['year'].append(j)
                        aggregate_transaction_dict['quarter'].append('Q' + k.strip('.json'))
                except Exception as e:
                    pass

    aggregate_df = pd.DataFrame(aggregate_transaction_dict)
    return aggregate_df



# Map TRANSACTION by STATE
def map_transaction_hover_by_state_all_year():
    PATH = "D:/Phonepe/data/map/transaction/hover/country/india/state/"
    statelist = os.listdir(PATH)
    map_transaction_dict = {
        'state': [],
        'year': [],
        'quarter': [],
        'district':[],
        'map_transaction_count': [],
        'map_transaction_amount': []
    }

    for i in statelist:
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)
        
        for j in state_year_list:
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files:
                jsFile = statewise_year_file_list + k
                data = open(jsFile, "r")
                output = json.load(data)
                try:
                    for map_data in output['data']['hoverDataList']:
                        district_name = map_data['name']
                        metric_count = map_data['metric'][0]['count']
                        metric_amount = map_data['metric'][0]['amount']
                        map_transaction_dict['district'].append(district_name.replace('district',''))
                        map_transaction_dict['map_transaction_count'].append(metric_count)
                        map_transaction_dict['map_transaction_amount'].append(metric_amount)
                        map_transaction_dict['state'].append(i.replace('-',' '))
                        map_transaction_dict['year'].append(j)
                        map_transaction_dict['quarter'].append('Q' + k.strip('.json'))
                except Exception as e:
                    pass

    aggregate_df = pd.DataFrame(map_transaction_dict)
    return aggregate_df





# Map USER by STATE
def map_user_hover_by_state_all_year():
    PATH = "D:/Phonepe/data/map/user/hover/country/india/state/"
    statelist = os.listdir(PATH)
    map_user_dict = {
        'state': [],
        'year': [],
        'quarter': [],
        'district':[],
        'registered_users': [],
        'app_opening': []
    }

    for i in statelist:
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)
        
        for j in state_year_list:
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files:
                jsnFile = statewise_year_file_list + k
                data = open(jsnFile, "r")
                output = json.load(data)
                try:
                    for district, map_data in output['data']['hoverData'].items():
                        registered_users = map_data['registeredUsers']
                        app_opening = map_data['appOpens']
                        map_user_dict['district'].append(district.replace('district',''))
                        map_user_dict['registered_users'].append(registered_users)
                        map_user_dict['app_opening'].append(app_opening)
                        map_user_dict['state'].append(i.replace('-', ' '))
                        map_user_dict['year'].append(j)
                        map_user_dict['quarter'].append('Q' + k.strip('.json'))
                except Exception as e:
                    pass

    aggregate_df = pd.DataFrame(map_user_dict)
    return aggregate_df




# Top TRANSACTION by STATE
def top_transaction_state_all_year():
    PATH = "D:/Phonepe/data/top/transaction/country/india/state/"
    statelist = os.listdir(PATH)
    top_transaction_dict = {
        
                            'state': [],
                            'year': [],
                            'quarter':[],
                            'district': [],
                            'count':[],
                            'amount':[]
                            }

    for i in statelist:# state name
        state_path = PATH + i + '/'
        state_year_list = os.listdir(
            state_path)
        
        for j in state_year_list:# year
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files: # year wise files
                jsnFile = statewise_year_file_list + k
                data = open(jsnFile, "r")
                output = json.load(data)
                try:
                    districts = output['data']['districts']
#                     pincodes = output['data']['pincodes']
        
                    for district in districts:
                        district_name = district['entityName']
                        count = district['metric']['count']
                        amount = district['metric']['amount']
                        
                        top_transaction_dict['state'].append(i.replace('-', ' '))
                        top_transaction_dict['year'].append(j)
                        top_transaction_dict['quarter'].append('Q' + k.strip('.json'))
                        top_transaction_dict['district'].append(district_name.replace('district',''))
                        top_transaction_dict['count'].append(count)
                        top_transaction_dict['amount'].append(amount)
                       
                except Exception as e:
                    print(f"Error: {str(e)}")

    top_trans_df = pd.DataFrame(top_transaction_dict)
    return top_trans_df





# Top USER by STATE
def top_user_state_all_year():
    PATH = "D:/Phonepe/data/top/user/country/india/state/"
    statelist = os.listdir(PATH)
    top_user_dict = {
        
                            'state': [],
                            'year': [],
                            'quarter':[],
                            'district': [],
                            'registered_users': []
                            }

    for i in statelist:# state name
        state_path = PATH + i + '/'
        state_year_list = os.listdir(
            state_path)
        
        for j in state_year_list:# year
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files: # year wise files
                jsnFile = statewise_year_file_list + k
                data = open(jsnFile, "r")
                output = json.load(data)
                try:
                    
                    for data in output['data']['districts']:
                        district = data['name']
                        registered_user = data['registeredUsers']
                        
                        top_user_dict['district'].append(district.replace('district', ''))
                        top_user_dict['registered_users'].append(registered_user)
                        top_user_dict['state'].append(i.replace('-',' ').lower())
                        top_user_dict['year'].append(j)
                        top_user_dict['quarter'].append('Q'+ k.strip('.json'))
                            
                except Exception as e:
                           print(f"Error: {str(e)}")
                        
    top_user_df = pd.DataFrame(top_user_dict)
    return top_user_df
                                                        



# Top TRANSACTION by Pincode
def top_transaction_state_pincode():
    
    PATH = "D:/Phonepe/data/top/transaction/country/india/state/"
    statelist = os.listdir(PATH)
    
    
    top_transpin_dict = {
                            'state': [],
                            'pincode': [],
                            'year': [], 
                            'quarter': [], 
                            'total_transaction_count': [], 
                            'total_transaction_amount': []
                        }
    
    for i in statelist:# state name
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)
        
        for j in state_year_list:# year
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files: # year wise files
                jsnFile = statewise_year_file_list + k
                data = open(jsnFile, "r")
                output = json.load(data)
                try:
                    pincodes = output['data']['pincodes']
                            
                    for data in pincodes:
                        pincode = data['entityName']
                        count = data['metric']['count']
                        amount = data['metric']['amount']
                       
                        top_transpin_dict['pincode'].append(pincode)
                        top_transpin_dict['total_transaction_count'].append(count)
                        top_transpin_dict['total_transaction_amount'].append(amount)
                        top_transpin_dict['state'].append(i.replace('-',' '))
                        top_transpin_dict['year'].append(j)
                        top_transpin_dict['quarter'].append('Q'+ k.strip('.json'))
                                
                except Exception as e:
                    print(f"Error: {str(e)}")
                        
    top_transpin_df = pd.DataFrame(top_transpin_dict)
    return top_transpin_df




# Top USER by Pincode
def top_user_state_pincode():
    
    PATH = "D:/Phonepe/data/top/user/country/india/state/"
    statelist = os.listdir(PATH)
    
    
    top_userpin_dict = {
                            'state': [],
                            'pincode': [],
                            'year': [], 
                            'quarter': [], 
                            'registered_users': []
                        }
    
    for i in statelist:# state name
        state_path = PATH + i + '/'
        state_year_list = os.listdir(state_path)
        
        for j in state_year_list:# year
            statewise_year_file_list = state_path + j + '/'
            statewise_year_files = os.listdir(statewise_year_file_list)
    
            for k in statewise_year_files: # year wise files
                jsnFile = statewise_year_file_list + k
                data = open(jsnFile, "r")
                output = json.load(data)
                
                try:
                    pincodes = output['data']['pincodes']
                            
                    for data in pincodes:
                        pincode = data['name']
                        registered_user = data['registeredUsers']
                        
                        top_userpin_dict['pincode'].append(pincode)
                        top_userpin_dict['registered_users'].append(registered_user)
                        top_userpin_dict['state'].append(i.replace('-',' '))
                        top_userpin_dict['year'].append(j)
                        top_userpin_dict['quarter'].append('Q'+ k.strip('.json'))
                
                except Exception as e:
                    print(f"Error: {str(e)}")
                        
    top_userpin_df = pd.DataFrame(top_userpin_dict)
    return top_userpin_df

                                                   



