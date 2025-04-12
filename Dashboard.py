import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Load the cleaned crime data
df = pd.read_csv("Crime_data/Cleaned_Crime_Data.csv")

# Find the Top 10 frequent crimes for filtering options.
top_10_crimes = df["Crm Cd Desc"].value_counts().nlargest(10).index.tolist() # Getting the TOP 10 most frequent crimes.
df["Crime Category"] = df["Crm Cd Desc"].apply(lambda x: x if x in top_10_crimes else "Others") # Categorizing the crimes as either in the TOP10 or in others.

# Sidebar for crime filtering options.
st.sidebar.title("Crime Type Filter") 
crime_selection = st.sidebar.multiselect("Select Crime Types", ["All Crimes"] + top_10_crimes + ["Others"], default=["All Crimes"]) # Adding all the options that can be selected and the default option is added.

# Function to Filter Data
def filter_data(selection): # Returns a part of the dataset that corresponds with the selections made.
    if "All Crimes" in selection or not selection:
        return df
    return df[df["Crime Category"].isin(selection)]

filtered_df = filter_data(crime_selection)

# --- Setting up the layout ---
col1, col2 = st.columns([3, 2])  # Setting up 2 columns that take up space in the ratio given by the array.

with col1: # Contents in the left column.
    st.subheader("Crime Distribution")
    # Piechart with plotly.
    crime_counts = filtered_df["Crime Category"].value_counts()
    fig_pie = px.pie(crime_counts, values=crime_counts.values, names=crime_counts.index, 
                 title="Crime Type Distribution", height=700, width=700)

    # Legend of the piechart.
    fig_pie.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.2))

    st.plotly_chart(fig_pie, use_container_width=True)

    
    # Crime Locations Map using folium.
    st.subheader("Crime Locations")
    
    # Reducing dataset because of performance issues ( My laptop crashed a couple of times trying to run the app with the whole dataset ).
    sampled_df = filtered_df.dropna(subset=["LAT", "LON"]).sample(n=min(len(filtered_df), 5000), random_state=42)
    # Plotting the reduced dataset using folium.
    crime_map = folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start=10)
    for _, row in sampled_df.iterrows():
        folium.CircleMarker([row["LAT"], row["LON"]], radius=3, color="red", fill=True).add_to(crime_map)
    
    st_folium(crime_map)

with col2: # Contents in the right column.
    st.subheader("Crime Trend Over Time")

    # Crime Distribution based on year.
    yearly_counts = filtered_df["YEAR_OCC"].value_counts().sort_index()
    fig_yearly = px.bar(yearly_counts, x=yearly_counts.index, y=yearly_counts.values, title="Crime by Year", height=500)
    st.plotly_chart(fig_yearly, use_container_width=True)

    # Crime Distribution based on month.
    monthly_counts = filtered_df["MONTH_OCC"].value_counts().sort_index()
    fig_monthly = px.bar(monthly_counts, x=monthly_counts.index, y=monthly_counts.values, title="Crime by Month", height=500)
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Crime Distribution based on hour.
    hourly_counts = filtered_df["HOUR"].value_counts().sort_index()
    fig_hourly = px.bar(hourly_counts, x=hourly_counts.index, y=hourly_counts.values, title="Crime by Hour", height=500)
    st.plotly_chart(fig_hourly, use_container_width=True)

# To run the app use: streamlit run dashboard.py
