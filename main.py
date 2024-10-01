import streamlit as st
import helper
st.title('Resturent Name Suggestion')
cuisine = ["Indian","Italian","Mexican","Lebanese","Japanese"]

st.sidebar.title('Select Cuisine')
selected_cuisine = st.sidebar.selectbox('Select Cuisine',cuisine)




if(cuisine):
    res = helper.name_and_menu_generator(cuisine)
    st.write(res["resturant name"])
    st.write("Suggestes Menu items are---")
    for item in res["Menu-items"]:
        st.write(item)
