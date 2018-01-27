import numpy as np
import scipy
import numpy as np
import random
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import cocktails_parse_util as cp
from sklearn.cluster import SpectralClustering,KMeans
def transformLine(line):
    ingredients = line.split(',')
    coctailList=''
    for ingridient in ingredients:
        ingredient = ingridient.split(':')[0]
        coctailList=coctailList+' '+ingredient


    return coctailList


def reduceAndPlot(data,labels,recipes):


    dat = pd.concat([data, pd.DataFrame(youAreHere(data)).T], ignore_index=True)


    tsne=TSNE(n_components=2,early_exaggeration=100)
    X_embedded = tsne.fit_transform(dat)
    print(X_embedded.shape)
    Sc=SpectralClustering(n_clusters=8, eigen_solver=None, random_state=None, n_init=10, gamma=1.0,
                                        n_neighbors = 10, eigen_tol = 0.0,)
    Sc=KMeans(n_clusters=8)
    cluster=Sc.fit_predict(X_embedded)
    plta=[]
    #py.plot([go.Scatter3d(x=X_embedded[:, 0], y=X_embedded[:, 1], z=X_embedded[:, 2],mode='markers+text', text=labels,textposition='bottom')])
    plta.append(go.Scatter(x=X_embedded[:-1, 0], y=X_embedded[:-1, 1],hovertext=recipes, name='cocktails',mode='markers+text', text=labels,textposition='bottom',marker=dict(
        size=14,
        color=cluster,                # set color to an array/list of desired values
        colorscale='Jet',   # choose a colorscale
        opacity=0.8
    )))
    plta.append(go.Scatter(x=X_embedded[-1:, 0], y=X_embedded[-1:, 1], mode='markers+text',name='you',text='YOU',textposition='bottom',marker=dict(
        size=20,
        color=15,                # set color to an array/list of desired values
        colorscale='Jet',   # choose a colorscale
        opacity=0.8
    )))
    py.plot(plta)
    dataset=pd.DataFrame({'coctkail':labels,'x':X_embedded[:, 0],'y':X_embedded[:, 1]})
    dataset.to_csv('TSECocktail.csv')
    return  X_embedded,tsne

def youAreHere(data):
    it=3
    out=0
    for i in range(it):
        rand=random.randint(1, 101)
        out=out+data.loc[rand,:]
    return out/it

def get_dictionary(line):
    ingredients = cp.get_ingredients(line)
    dict = {}
    for ingredient in ingredients:
        dict[ingredient[0]]=ingredient[1]
    return dict

data=pd.read_csv('cocktails_data.csv', encoding='iso-8859-1', header=None,sep='\t')

data['dict']=data[data.columns[1]].astype(str).apply(get_dictionary)
df = data['dict'].apply(pd.Series).fillna(0)

print(cp.get_ingredientsline_grams("rum:1 1/2 ounces,lime juice:3/4 ounce,grenadine:2 dashes,"))

recipes=data[data.columns[1]].astype(str).apply(cp.get_ingredientsline_grams)
'''
data[data.columns[1]]=data[data.columns[1]].astype(str).apply(transformLine)
vb=TfidfVectorizer()

transformde=vb.fit_transform(data[data.columns[1]])

'''

labels=data[data.columns[0]]
#df['label']=labels
df.to_csv('CData')
reduceAndPlot(df,labels,recipes)
