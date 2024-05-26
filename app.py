




import streamlit as st
import requests
import pickle


movies_list = pickle.load(open('movies.pkl','rb'))

cs = pickle.load(open('cosinesimilarity.pkl','rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommand(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    sorted_similar_movies = sorted(list(enumerate(cs[movie_index])),reverse = True, key= lambda x: x[1])[1:6]
    
    recommand_movies = []
    recommand_movies_posters = []
    for i in sorted_similar_movies:
        firstIndex = i[0]
        posterPath = fetch_poster(movies_list.iloc[firstIndex].movie_id)
        recommand_movies_posters.append(posterPath)
        recommand_movies.append(movies_list.iloc[firstIndex].title)
        
    return recommand_movies,recommand_movies_posters


st.title('Movie Recommand System')

option = st.selectbox('select your movie',movies_list['title'].values,
                        index=None,
                        placeholder="select your movie...",
                    )



if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommand(option)
    col1, col2, col3, col4, col5 = st.columns(5,gap)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")