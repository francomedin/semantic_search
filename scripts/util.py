import pandas as pd
import pinecone
from sentence_transformers import SentenceTransformer
import streamlit as st

model = None
index = None

def load_model():
    global model
    if model is None:
       model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    

def load_index():
    global index
    if index is None:
        pinecone_api = st.secrets["PINECODE_API_KEY"]
        enviroment = st.secrets["PINECODE_ENVIROMENT"]
        index_name = st.secrets["INDEX_NAME"]
        pinecone.init(api_key=pinecone_api, environment = enviroment)
        index = pinecone.Index(index_name)

load_model()
load_index()

def search(query, genre, rating, top_k):
  query_vector = model.encode(query).tolist()

  if rating:
    filter_rating = rating
  else:
    filter_rating = 0

  if genre:
    conditions = {
        'Generes' : {
            '$in' : [genre]
        },
        'Rating' : {
            '$gte' : filter_rating
        }
    }
  else:
    conditions = {
        'Rating' : {
            '$gte' : filter_rating
        }
    }

  responses = index.query(
      vector = query_vector,
      top_k = top_k,
      include_metadata = True,
      filter = conditions
  )

  response_data = []
  for response in responses['matches']:
    response_data.append({
        'Title' : response['metadata']['movie title'],
        'Overview' : response['metadata']['Overview'],
        'Director' : response['metadata']['Director'],
        'Genre' : response['metadata']['Generes'],
        'year' : response['metadata']['year'],
        'Rating' : response['metadata']['Rating'],
        'Score' : response['score'],
    })
  
  df = pd.DataFrame(response_data)
  return df


