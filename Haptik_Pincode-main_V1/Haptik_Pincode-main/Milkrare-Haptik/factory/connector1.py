import pandas as pd
import os


def milking(request_json):
    try:
        response = {}
        df = pd.read_csv(r"C:\Users\satishkumar.s\Downloads\Haptik_Pincode-main (1)\Haptik_Pincode-main\Milkrare-Haptik\factory\Haptikdata.csv",encoding='latin-1')
        #url = "https://github.com/wazsee/Haptik_Pincode/blob/main/Milkrare-Haptik/factory/Haptikdata.csv"
        #df = pd.read_csv('https://github.com/wazsee/Haptik_Pincode/blob/main/Milkrare-Haptik/factory/Haptikdata.csv', on_bad_lines='skip')
        #url = "https://github.com/wazsee/Haptik_Pincode/blob/main/Milkrare-Haptik/factory/Haptikdata.csv?raw=true"
        #df = pd.read_csv(url)
            
        #print("df")
        

        #request_json['Milk1_Dry2'] = 1 if request_json['Milk1_Dry2'] == "milk" else 2

        response_values = df.loc[
            (df['PinCode']==request_json['PinCode'])
            ]
        print(df.head())
        #if request_json['Phone_Number'] ==request_json['Phone_Number']:
        if str(request_json['PinCode']) in df.values:
            #response['Pin code Exists']
            response['RegionName'] = response_values['RegionName'].values[0] 
            #response['Pin code Exists']

            #print('Pin code Exists')
        if str(request_json['PinCode']) not in df.values:
            response['Pin code Does not Exists']
            #print('Pin code Does nottttt Exists')

        #response['Farmer Name'] = response_values['Farmer Name'].values[0]
        # response['Region Name'] = response_values['Region Name'].values[0]
        # response['District Name'] = response_values['District Name'].values[0]
        # response['Pin Code'] = response_values['Pin Code'].values[0] 
        # #response['Plant Name'] = response_values['Plant Name'].values[0]
        # response['Plant Code'] =int(response_values['Plant Code'].values[0])
        # response['MCC Name'] = response_values['MCC Name'].values[0]
        # response['MCC Code'] = int(response_values['MCC Code'].values[0])    

        return response
    except Exception as e:
        return str(e)
    
