import streamlit as st
import pickle
import pandas as pd
#function to recommend places
def recommend(place,city):
    place_index = travel_places[travel_places['Place_Name'] == place].index[0]
    distances = similarity[place_index]
    places_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_places = []
    #iterates and returns data one by one 
    for i in places_list:
        recommended_places.append(travel_places.iloc[i[0]].Place_Name if travel_places.iloc[i[0]].City == city else "")
        result = list(filter(None, recommended_places))
    return result

#function to remove data redundancy
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

#gather data from csv files
similarity = pickle.load(open('similarity.pkl','rb'))
travel_list = pickle.load(open('Travel_dict.pkl','rb'))

travel_places = pd.DataFrame(travel_list)

#--------------Web Content---------------------------#
st.title('Travel Recommendation System')

selected_travel_name =  st.selectbox(
    'What would you like to be visit ?',
    remove_duplicates(travel_places['Place_Name'].values)
)

selected_travel_city =  st.selectbox(
    'Filter by Location',
    remove_duplicates(travel_places['City'].values)
)

if st.button('Recommend'):
    recommendations = recommend(selected_travel_name,selected_travel_city)
    for i in recommendations:
        st.write(i)