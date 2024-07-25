import streamlit as st
from db_call import raw_data_to_df
import numpy as np
from datetime import datetime, timedelta
import pytz

def normalize_to_midniight(date):

    return datetime(date.year,date.month,date.day, tzinfo=pytz.UTC)


@st.cache_data
def total_users_(df_users):
    return len(df_users)

@st.cache_data
def find_active_users(df_users):

    numb = np.unique(df_users[df_users.PausedAt.isna()].Id).shape[0]

    return numb

@st.cache_data
def asnwered_today(df_point):
    
    today = datetime.now(pytz.UTC)
    star_date = datetime(today.year, today.month, today.day, tzinfo=pytz.UTC)

    return np.unique(df_point[df_point.UserPointCreatedAt >= star_date].UserId).shape[0]

@st.cache_data
def entered(df_aps_users):
    entered_today = df_aps_users[df_aps_users.CreatedAt >= normalize_to_midniight(datetime.now())]
    entered_this_week = df_aps_users[df_aps_users.CreatedAt >= datetime.now(pytz.UTC) - timedelta(weeks=1)]

    return entered_today,entered_this_week

@st.cache_data
def droppers(df_aps_users):
    
    df_dropers = df_aps_users[df_aps_users.PausedAt.isna() == False]
    drop_today  = len(df_dropers[df_dropers.PausedAt >= normalize_to_midniight(datetime.now())])
    droped_this_week = len(df_dropers[df_dropers.PausedAt >= datetime.now(pytz.UTC) - timedelta(weeks=1)])

    return len(df_dropers), drop_today, droped_this_week