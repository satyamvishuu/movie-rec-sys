print("Script is starting", flush=True)


import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    print(f"fetch_poster called with ID: {movie_id}", flush=True)
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4ffe78b827baee19a289403b8e11b730&language=en-US"
        response = requests.get(url, timeout=15)
        data = response.json()
        print(f"Movie ID: {movie_id} - API Response: {data}")
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            print(f"No poster found for Movie ID: {movie_id}", flush=True)
            return "https://dummyimage.com/500x750/000/fff&text=No+Image"
    except Exception as e:
        print(f"Error fetching poster for Movie ID {movie_id}: {e}", flush=True)
        return "https://dummyimage.com/500x750/000/fff&text=No+Image"
    

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]: 
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters



st.title("🎬 Movie Recommender System")


movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

try:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    print(f"Recommended movies: {recommended_movie_names}", flush=True)

    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.text(name)
            st.image(poster)
except Exception as e:
    print(f"Error in recommend function: {e}", flush=True)
    st.error("Failed to fetch recommendations.")
