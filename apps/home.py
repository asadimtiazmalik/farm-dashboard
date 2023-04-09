import streamlit as st
import leafmap.foliumap as leafmap
import os  
from folium.plugins import FloatImage
from folium.raster_layers import ImageOverlay
import geopandas as gpd
import pandas as pd
import plost
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
    # with c1:
    #     scale = alt.Scale(
    #         domain=["rain"],
    #         range=["#1f77b4"],
    #     )
    #     color = alt.Color("weather:N", scale=scale)

    #     # We create two selections:
    #     # - a brush that is active on the top panel
    #     # - a multi-click that is active on the bottom panel
    #     brush = alt.selection_interval(encodings=["x"])
    #     click = alt.selection(encodings=["color"])

    #     # Top panel is scatter plot of temperature vs time
    #     points = (
    #         alt.Chart()
    #         .mark_point()
    #         .encode(
    #             alt.X("monthdate(date):T", title="Date"),
    #             alt.Y(
    #                 "temp_max:Q",
    #                 title="Maximum Daily Temperature (C)",
    #                 scale=alt.Scale(domain=[-5, 40]),
    #             ),
    #             color=alt.condition(brush, color, alt.value("lightgray")),
    #             size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    #         )
    #         .properties(width=550, height=300)
    #         .add_selection(brush)
    #         .transform_filter(click)
    #     )

    #     # Bottom panel is a bar chart of weather type
    #     # bars = (
    #     #     alt.Chart()
    #     #     .mark_bar()
    #     #     .encode(
    #     #         x="count()",
    #     #         y="rain",
    #     #         color=alt.condition(click, color, alt.value("lightgray")),
    #     #     )
    #     #     .transform_filter(brush)
    #     #     .properties(
    #     #         width=550,
    #     #     )
    #     #     .add_selection(click)
    #     # )

    #     chart = alt.vconcat(points, data=source, title="Islamabad Weather: 2022-2023")

    tab1, tab2 = st.tabs(["Climate Data", "Vegetation Indices"])

    # with tab1:
            # st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
            # src = pd.DataFrame({"Date":['16th Dec', '26th Dec', '30th Dec', '3rd Jan'], "NDVI": [0.2,0.5,0.9,0.6], "RVI": [0.1,0.3,0.6,0.5], "NIR": [0.1,0.35,0.66,0.5]})
            chart_data = pd.DataFrame(
            np.random.randn(4, 3), index= ['16th Dec', '26th Dec', '30th Dec', '3rd Jan'],
            columns=['NDVI', 'RVI', 'NIR'])

            st.line_chart(chart_data)
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
