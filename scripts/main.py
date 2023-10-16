import streamlit as st
from util import search



# Define possible genres
genres = ['All Generes','Action', 'Drama', 'Adventure', 'Sci-Fi', 'Animation', 'Crime',
       'Comedy', 'Thriller', 'Fantasy', 'Horror', 'History', 'Mystery',
       'Biography', 'War', 'Western', 'Sport', 'Family', 'Romance',
       'Music', 'Musical', 'Film-Noir', 'Game-Show', 'Adult',
       'Reality-TV']

# Create Streamlit UI components
st.title("Buscador de películas")
st.write("Introduce tu consulta, selecciona un género y define una puntuación mínima para buscar películas.")

# Inputs
query = st.text_area("Consulta", value="", height=150, max_chars=500, help="E.g.: A scary movie about clowns")
genre = st.selectbox("Género de la película", genres)
min_rating = st.slider("Puntuación mínima", min_value=1, max_value=10, value=5)
top_k = st.number_input("Número de resultados", min_value=1, max_value=10, value=5)

# Button to trigger search
if st.button("Buscar"):
    # Call your search function with the selected inputs and display the results here
    if genre == "All Generes":
        genre = None
    results = search(query, genre, min_rating, top_k)
    st.write("Resultados:")
    st.dataframe(results)



