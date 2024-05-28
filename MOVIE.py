import streamlit as st
import pickle
import pandas as pd
import numpy as np
import json
from streamlit_lottie import st_lottie

def  load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

file= load_lottiefile("81986-movie.json") 
st_lottie(file,speed=1,reverse=False,quality="high",loop=True,height=400)


st.title("Movie Recommendatation system")

movie_df=pickle.load(open("movie_recm.pkl","rb"))

similarity=pickle.load(open("similarity.pkl","rb"))

list_movie=np.array(movie_df["title"])

option = st.selectbox(
"Select Movie ",
(list_movie))

def show_url(movie):
     x=[]
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     for i in distances[1:6]:

          x.append(movie_df.iloc[i[0]].urls)
     return(x)

def movie_recommend(movie):
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:6]:
          l.append("{}".format(movie_df.iloc[i[0]].title))
          
     return(l)

if st.button('Recommend Me'):
     st.write('Movies Recomended for you are:')
     
     df = pd.DataFrame({
          'Movie Recommended': movie_recommend(option),
          'Movie Url': show_url(option)
     })

     st.table(df)
