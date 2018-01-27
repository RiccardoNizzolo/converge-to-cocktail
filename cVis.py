import numpy as np
import scipy
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer


def transformLine(line):
    ingredients = line.split(',')
    coctailList=''
    for ingridient in ingredients:
        ingredient = ingridient.split(':')[0]
        coctailList=coctailList+' '+ingredient
    return coctailList



def reduceAndPlot(data,labels):


    #svd = TruncatedSVD(n_components=100, n_iter=15, random_state=42)
   #X_svd=svd.fit_transform(data)


    X_embedded = TSNE(n_components=2).fit_transform(data)
    print(X_embedded.shape)

    py.plot([go.Scatter(x=X_embedded[:, 0], y=X_embedded[:, 0], mode='markers+text', text=labels)])
    return  X_embedded


data=pd.read_csv('cocktails_data.csv', encoding='	iso-8859-1', header=None,sep='\t')
data[data.columns[1]]=data[data.columns[1]].astype(str).apply(transformLine)

vb=TfidfVectorizer()

transformde=vb.fit_transform(data[data.columns[1]])
labels=data[data.columns[0]]

reduceAndPlot(transformde.todense(),labels)
