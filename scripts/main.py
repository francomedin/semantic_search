import streamlit as st
from util import search



# Define possible genres
genres = ['All Genres','Action', 'Drama', 'Adventure', 'Sci-Fi', 'Animation', 'Crime',
       'Comedy', 'Thriller', 'Fantasy', 'Horror', 'History', 'Mystery',
       'Biography', 'War', 'Western', 'Sport', 'Family', 'Romance',
       'Music', 'Musical', 'Film-Noir', 'Game-Show', 'Adult',
       'Reality-TV']

# Create Streamlit UI components
st.title("Movie Search")
st.write("Enter your query, select a genre and define a minimum score to search for movies.")

# Inputs
query = st.text_area("Query", value="", height=150, max_chars=500, help="E.g.: A scary movie about clowns")
genre = st.selectbox("Movie Genre", genres)
min_rating = st.slider("Minimum Score", min_value=1, max_value=10, value=5)
top_k = st.number_input("Number of Results", min_value=1, max_value=10, value=5)

# Button to trigger search
if st.button("Search!"):
    # Call your search function with the selected inputs and display the results here
    if genre == "All Genres":
        genre = None
    results = search(query, genre, min_rating, top_k)
    st.write("Result:")
    st.dataframe(results)

    st.line
    st.write('Cards')
    try:
        for index, row in results.iterrows():
            st.write(f"**{row['Title']}**")
            st.write(row['Overview'])
            st.write(f"**Director:** {row['Director']}")
            st.write(f"**Genre:** {row['Genre']}")
            st.write(f"**Year:** {row['Year']}")
            st.write(f"**Rating:** {row['Rating']}")
            st.write(f"**Score:** {row['Score']}")
    except:
        pass

    st.line
    st.write('Grid')
    try:
        col1, col2, col3 = st.beta_columns(3)  # Split the screen into three columns
        for index, row in results.iterrows():
            with col1:
                st.image("movie_image_url.jpg", use_container_width=True)
            with col2:
                st.write(f"**{row['Title']}**")
                st.write(f"**Director:** {row['Director']}")
                st.write(f"**Rating:** {row['Rating']}")
            with col3:
                st.write(f"**Genre:** {row['Genre']}")
                st.write(f"**Year:** {row['Year']}")
                st.write(f"**Score:** {row['Score']}")

    except:
        pass

 







