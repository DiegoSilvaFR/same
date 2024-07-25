from db_call import raw_data_to_df
import streamlit as st

join_query = """SELECT 
    x."CreatedAt" AS "UserCreatedAt",
    x."PausedAt",
    x."LastDailyAnsweredAt",
    x."FirstName",
    x."LastName",
    y."EffectiveAt" AS "UserPointCreatedAt",
    y."Score",
    y."UserId"
FROM 
    public."AspNetUsers" x
INNER JOIN 
    public."DataPoints" y
ON 
    x."Id" = y."UserId"
     
"""
@st.cache_data()
def dfs():

    df_tenants = raw_data_to_df("""select * from public."Tenants" """)
    df_aps_users = raw_data_to_df("""select * from public."AspNetUsers" """)
    df_points = raw_data_to_df(join_query)
    questions = raw_data_to_df(""" select * from public."QuestionTranslations" """ )

    return df_tenants, df_aps_users, df_points, questions