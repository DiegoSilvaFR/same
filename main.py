#main 
import streamlit as st
from transformations.stikers import *
from data.dfs_warmup import dfs

import warnings
warnings.filterwarnings("ignore")
import streamlit.components.v1 as components


st.set_page_config(page_icon="📊", page_title="Superdash Analytics")

# Custom CSS to reduce space between title and number
st.markdown(
    """
    <style>
    div.css-1cpxqw2.e1tzin5v0 > div > div {
        line-height: 1;  /* Adjust this value to control the space */
        padding-bottom: 0px; /* Adjust this value to control the bottom padding */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('Analytics')

def stickers(df_aps_users, df_points):
    
    total_users = total_users_(df_aps_users)
    active_users = find_active_users(df_aps_users)
    asnwered = asnwered_today(df_points)
    
    entered_today,entered_this_week = entered(df_aps_users)
    df_dropers, drop_today, droped_this_week = droppers(df_aps_users)

    col1,col2,col3,col4 = st.columns(4)

    with col1:

        st.info("Total de Usuários", icon="📌")
        st.metric(label=" ",value=f"{total_users}")
    
    with col2:

        st.info("Total de Usuários Ativos", icon="📌")
        st.metric(label=" ",value=f"{active_users}")
    
    with col3:

        st.info("Total que responderam Hoje", icon="📌")
        st.metric(label=" ",value=f"{asnwered}")

    with col4:

        st.info("Total que entraram Hoje", icon="📌")
        st.metric(label=" ",value=f"{(len(entered_today))}")
    
    col5,col6,col7,col8 = st.columns(4)

    with col5:

        st.info("Total que entraram nos ultímos 7 dias", icon="📌")
        st.metric(label=" ",value=f"{len(entered_this_week)}")
    
    with col6:

        st.info("Total que Abandonaram", icon="📌")
        st.metric(label=" ",value=f"{df_dropers}")
    
    with col7:

        st.info("Total que Abandonaram Hoje", icon="📌")
        st.metric(label=" ",value=f"{drop_today}")

    with col8:

        st.info("Total que Abandonaram nos ultímos 7 dias", icon="📌")
        st.metric(label=" ",value=f"{droped_this_week}")

    
    
   

df_tenants, df_aps_users, df_points, questions = dfs()


stickers(df_aps_users,df_points)