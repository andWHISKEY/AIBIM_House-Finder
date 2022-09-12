import os
import pandas as pd
from sklearn import preprocessing

EXCEL_DIR='D:/SimGNNDATA/ExcelFiles' #기존 Excel File Folder 경로
CSV_DIR='D:/SimGNNDATA/CSVFiles' #새로이 저장할 CSV File Folder 경로
dataset_folder=os.listdir(EXCEL_DIR)

for i,file in enumerate(dataset_folder):
    df_excel = pd.DataFrame()
    file_excel_name=file.split('.')[0]
    df= pd.read_excel(os.path.join(EXCEL_DIR,file),header=3,usecols="C,D,E,F,G,AA,AB,AC")
#     print(i,file,df)
    df_excel["Unique"]=df["건축물+층수"].map(str)
    df_excel["ID"] = df["0/1/2/3/F"].map(str) + "_" + df["NAME"]+"_"+df["NAME(N)"].map(str)
    df_excel["Label"]=df['CLASS']
    df_excel["Adj_ID"]= df["0/1/2/3/F"].map(str) + "_" + df["NAME.1"]+"_"+df["NAME(N).1"].map(str)
    df_excel["Adj_Label"]=df['CLASS.1']
    
    f1=file_excel_name+'-1'
    f2=file_excel_name+'-2'
    str1_expr = "Unique == @f1"    
    f1_df = df_excel.query(str1_expr) 
    str_expr = "Unique == @f2"    
    f2_df = df_excel.query(str_expr) 
    
    #-------floor 1------------
    encoder = preprocessing.LabelEncoder()
    encoder.fit(f1_df['ID'])
    f1_df['ID_encode']=encoder.transform(f1_df['ID'])
    f1_df['Adj_ID_encode']=encoder.transform(f1_df['Adj_ID'])
    f1_df.drop(['Unique'],axis=1,inplace=True)
    f1_df.to_csv(os.path.join(CSV_DIR,f1)+".csv", mode='w',index=False)
    #--------------------------
    
    if not f2_df.empty:
        encoder2 = preprocessing.LabelEncoder()
        encoder2.fit(f2_df['ID'])
        f2_df['ID_encode']=encoder2.transform(f2_df['ID'])
        f2_df['Adj_ID_encode']=encoder2.transform(f2_df['Adj_ID'])
        f2_df.drop(['Unique'],axis=1,inplace=True)
        f2_df.to_csv(os.path.join(CSV_DIR,f2)+".csv", mode='w',index=False)
