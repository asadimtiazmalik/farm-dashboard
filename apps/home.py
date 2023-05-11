import streamlit as st
import leafmap.foliumap as leafmap
import os  
from folium.plugins import FloatImage
from folium.raster_layers import ImageOverlay
import geopandas as gpd
import pandas as pd
# import plost
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("Wheat Health Monitoring Dashboard")

    # st.markdown(
    #     """
    # A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    # To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    # https://share.streamlit.io/giswqs/streamlit-template?page=upload

    # """
    # )
    with open('C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\apps\\styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown('### Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Area", "11 Acres")
    col2.metric("Average NDVI", "0.155", "-2%")
    col3.metric("Phenotypes", "100 +")

    # Row B
    source = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

    c1, c2 = st.columns((7,3))
    

    tab1, tab2 = st.tabs(["Climate Data", "Vegetation Indices"])

    # with tab1:
            # st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
            # src = pd.DataFrame({"Date":['16th Dec', '26th Dec', '30th Dec', '3rd Jan'], "NDVI": [0.2,0.5,0.9,0.6], "RVI": [0.1,0.3,0.6,0.5], "NIR": [0.1,0.35,0.66,0.5]})
            data = pd.DataFrame(
            [[0.01,0.25], 
            [0.5,0.17], 
            [0.02,0.03], 
            [0.5,0.25]], index= ['26-12-22', '20-01-23', '24-02-23', '20-04-23'],
            columns=['NDVI', 'SAVI'])
            # Add more data points
            # Convert index to datetime objects
            # data.index = pd.to_datetime(data.index, format='%d-%m-%y')

            # # Add more data points
            # num_points = 50
            # new_index = pd.date_range(start=data.index[0], end=data.index[-1], periods=num_points)
            # new_data = pd.DataFrame(index=new_index, columns=data.columns)

            # for column in data.columns:
            #     interp_func = np.interp(new_index, data.index, data[column])
            #     new_data[column] = interp_func
            # Plot the data using Streamlit line chart
            # st.line_chart(new_data)

            st.line_chart(data)
            # fig = cd._get_figure()
            # ax = fig.gca()
            # Rotate the xticks
            # ax.set_xticklabels(cd['x'], rotation=45)
            
    



    with c2:
        st.markdown('### Donut chart')
        # Define the data for the donut chart
        source = pd.DataFrame({"category": ["Healthy Area", "Infected Area", "Out of bounds"], "area in Acres": [5.22, 1.55, 2.74]})

        fig = alt.Chart(source).mark_arc(innerRadius=50).encode(
            theta=alt.Theta(field="area in Acres", type="quantitative"),
            color=alt.Color(field="category", type="nominal"),
            opacity = alt.value(0.6),
        )
        # Display the chart using Streamlit
        st.altair_chart(fig, use_container_width=True)

    # Row C
    # st.markdown('### Line chart')
    # st.line_chart(seattle_weather, x = 'date', y = ['temp_min', 'temp_max'], height = 200)
