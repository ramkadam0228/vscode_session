import pandas as pd

source_df=pd.read_csv(r"C:\Users\ramka\Documents\vscode_session\TRADE_INPUT.csv")
print(source_df)



def filterdata(**kargs):
    for i,j in kargs.items():
        filtered_df=source_df[source_df[i]==j] 
    
    print(filtered_df)
    return(filtered_df)


overiding_df=filterdata(PRODUCT_ID_VALUE_1='COMMODITIES', PRODUCT_ID_VALUE_2='GOLD', BU=44  )

print("---------------------------------------------------")

def overrideTheFieldsFromGiven(**rams):
    for i, j in rams.items():
        overiding_df[i]=(overiding_df[i].to_string(index=False)).replace(overiding_df[i].to_string(index=False),j)
        print(overiding_df)
        return overiding_df
   

tapiout_df=overrideTheFieldsFromGiven(PRICE = '77', PRICE_CURRENCY = 'XYZ' )

# tapiout_df.to_csv(r'C:\Users\ramka\OneDrive - Atyeti Inc\Desktop\data.csv')






