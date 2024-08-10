import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def create_casual_user(df): 
    casual_user = year['casual'].sum()

    return casual_user

def create_registered_user(df):
    registered_user = year['registered'].sum()

    return registered_user

def create_weekday(df):
    weekday = year['weekday'].sum()

    return weekday

df = pd.read_csv("data_main.csv")
year = df[df['yr'] == 0]

casual = create_casual_user(df)
registered = create_registered_user(df)

st.header("Bike Sharing Dashboard 🚲")
st.image("D:\project dicoding\dashboard\images.jpeg")
st.subheader("Yearly User Casual & Registered (2011)")

col1, col2 = st.columns(2)
with col1:
    total_casual = casual
    st.metric("Total Number of Casual Bike Users for 2011", value=total_casual)
    
    monthly_df = year.groupby(by="mnth").agg({
    "casual" : "sum"
    })
    monthly_df.index = monthly_df.index.map({
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 
        5: 'May', 6: 'June', 7: 'July', 8: 'August', 
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    })
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(monthly_df["casual"], marker='o', linewidth=2, color="#72BCD4") 
    ax.set_title("Number of Casual User Rental Bike", loc="center", fontsize=20)
    ax.set_xticklabels(monthly_df.index, fontsize=10, rotation=25)
    st.pyplot(fig)

with col2:
    total_registered = registered
    st.metric("Total Number of Registered Bike Users for 2011", value=total_registered)

    monthly_df = year.groupby(by="mnth").agg({
    "registered" : "sum"
    })
    monthly_df.index = monthly_df.index.map({
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 
        5: 'May', 6: 'June', 7: 'July', 8: 'August', 
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    })
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(monthly_df["registered"], marker='o', linewidth=2, color="#72BCD4") 
    ax.set_title("Number of Registered User Rental Bike", loc="center", fontsize=20)
    ax.set_xticklabels(monthly_df.index, fontsize=10, rotation=25)
    st.pyplot(fig)


st.subheader("Bike Sharing Usage by Day")
weekday_anlys = year.groupby(by="weekday").agg({
    "cnt" : "nunique",
})
weekday_anlys.index = weekday_anlys.index.map({
    0:'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5:'Friday', 6:'Saturday'
})
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x=year["weekday"], 
    y=year["cnt"].rename("Number of User"),
    data=weekday_anlys.sort_values(by="weekday", ascending=False),
    palette=colors,
    ax=ax
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xticklabels(weekday_anlys.index, fontsize=20)
st.pyplot(fig)

st.subheader("Hourly Bike Sharing")
hour_analysis = year.groupby(by="hr").agg({
    "cnt" : "sum",
})
fig, ax = plt.subplots(figsize=(10,10))
sns.barplot(
    x=year["hr"].rename("Hours"), 
    y=year["cnt"].rename("Number of Users"), 
    data=hour_analysis.sort_values(by="hr", ascending=False), 
    ax=ax      
    ) 
ax.set_xticklabels(hour_analysis.index, fontsize=10)
st.pyplot(fig)
