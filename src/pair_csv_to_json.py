import pandas as pd
import os
import numpy as np
import json
import networkx as nx
from query import Test

dataset_folder=Test #Query문에 의해 추출된 Model에 돌릴 Test dataset list
CSV_PATH='D:/SimGNNDATA/CSVFiles' #기존 CSV File Folder 경로
JSON_PATH='D:/SimGNNDATA/Test' #새로이 저장할 Json File Folder 경로

class NumpyEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

    
for i,filei in enumerate(dataset_folder):
    data = dict()
    df1= pd.read_csv(os.path.join(CSV_PATH,filei+'.csv'))
    data["graph_1"]=np.c_[df1['ID_encode'].tolist(),df1['Adj_ID_encode'].tolist()]
    data["labels_1"]=df1[['Label', 'ID_encode']].drop_duplicates().sort_values(by=['ID_encode'])['Label'].astype(str).tolist()
    graph_1=nx.from_pandas_edgelist(df1,'ID','Adj_ID',create_using=nx.Graph())
    for j,filej in enumerate(dataset_folder[i+1:]):
        df2= pd.read_csv(os.path.join(CSV_PATH,filej+'.csv'))
        data["graph_2"]=np.c_[df2['ID_encode'].tolist(),df2['Adj_ID_encode'].tolist()]
        data["labels_2"]=df2[['Label', 'ID_encode']].drop_duplicates().sort_values(by=['ID_encode'])['Label'].astype(str).tolist()
        graph_2=nx.from_pandas_edgelist(df2,'ID','Adj_ID',create_using=nx.Graph())
        for v in nx.optimize_graph_edit_distance(graph_1, graph_2):
            max2 = v
            break
        data["ged"]=max2 
    
        with open(JSON_PATH+"/"+filei.split(sep='.')[0]+"&"+filej.split(sep='.')[0]+".json",'w') as f:
            json.dump(data, f, cls=NumpyEncoder)
            f.close()
            print(f,'----------------------------------------')