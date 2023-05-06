import os
import geopandas as gpd
import streamlit as st
import os  
import leafmap.foliumap as leafmap
from folium.plugins import FloatImage
from folium.raster_layers import ImageOverlay
import matplotlib.pyplot as plt
import pandas as pd 
import altair as alt


def save_uploaded_file(file_content, file_name):
    """
    Save the uploaded file to a temporary directory
    """
    import tempfile
    import os
    import uuid

    _, file_extension = os.path.splitext(file_name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(file_content.getbuffer())

    return file_path

def calculate_healthy_area():
    """
    Calculate healthy, infected and out of bounds area
    """

def display_healthy_region(healthy=5.22, infected=1.55, out_of_bounds=2.74):
    """
    Display a donut chart indicating the healthy and infected regions.

    Parameters:
    -----------
    healthy: float, optional
        The area in acres of healthy region.
    infected: float, optional
        The area in acres of infected region. 
    out_of_bounds: float, optional
        The area in acres of out of bounds region.

    Returns:
    --------
    altair.Chart
        A donut chart representing the areas of healthy, infected, and out of bounds regions.
    """
    # Define the data for the donut chart
    source = pd.DataFrame({"category": ["Healthy Area", "Infected Area", "Out of bounds"], 
                           "area in Acres": [healthy, infected, out_of_bounds]})

    figure = alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="area in Acres", type="quantitative"),
        color=alt.Color(field="category", type="nominal"),
        opacity = alt.value(0.6),
    )

    return figure


def display_map(center, zoom, geo_json, orthomosaic, layer_title, legend_url, detected=False, opacity=0.7):
    
    """
    Display a map with a satellite tile layer, an orthomosaic image, a health indicator layer,
    and a legend image. 

    Parameters
    ----------
    center: tuple
        A tuple of two floats representing the latitude and longitude of the map center.
    zoom: int
        An integer representing the initial zoom level of the map.
    geo_json: dict
        A GeoJSON object representing the health indicator layer.
    orthomosaic: str
        The URL or path to the orthomosaic image to be displayed on the map.
    layer_title: str
        The name of the orthomosaic layer to be displayed on the map.
    legend_url: str
        The URL or path to the legend image to be displayed on the map.
    detected: bool, optional
        If True, the health indicator layer will be displayed on the map. Default is False.
    opacity: float, optional
        The initial opacity of the orthomosaic layer. Default is 0.7.

    Returns
    -------
    leafmap.Map
        The generated map object.
    """


    map = leafmap.Map(center = center, zoom=zoom)
    map.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
    )

    if detected:
        map.add_geojson(geo_json, layer_name="Health Indicator")

    ImageOverlay(orthomosaic,
                [[33.672652308289614,73.12770497102615], [33.67436783460362,73.1307913403036]],
                opacity=opacity, name=layer_title
                ).add_to(map)
    
    FloatImage(legend_url, bottom=30, left=90, width=10).add_to(map)

    return map 



def app():

    st.title("Upload Vector Data")

    row1_col1, row1_col2 = st.columns([2, 1])
    width = 930
    height = 600
    out_dir = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\images"
    geojs = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\geojson"
    isDetected = False


    with open('C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\apps\\styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    with row1_col2:
        container = st.container()
        with container:
            date = st.selectbox(
                "Select a date", ["16-12-23", "26-12-23", "30-12-23"], index=1
            )

            vg_idx = st.radio(
                "Select a Vegetation Index",
                ('NDVI', 'RVI', 'NIR')
            )

            # Display the chart using Streamlit
            fig = display_healthy_region()
            st.altair_chart(fig, use_container_width=True)




        # container = st.container()

        if date or vg_idx:
            # geojson = os.path.join(out_dir, 'ndvi.json')
            if date:
                if date == "16-12-23":
                    dem = os.path.join(out_dir, 'dec-16_rgba_ndvi.png')
                    if vg_idx == 'NDVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'RVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"
                    elif vg_idx == 'NIR':
                        vg = "https://user-images.githubusercontent.com/65748116/230503703-42e5b96e-5eb7-40c9-9674-b7420e0bdb2c.png"
                elif date == "26-12-23":
                    dem = os.path.join(out_dir, 'dec-26_rgba_ndvi.png')
                    geo = os.path.join(geojs, '26.json')
                    isDetected = True
                    if vg_idx == 'NDVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'RVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"
                    elif vg_idx == 'NIR':
                        vg = "https://user-images.githubusercontent.com/65748116/230503703-42e5b96e-5eb7-40c9-9674-b7420e0bdb2c.png"                    
                elif date == "30-12-23":
                    dem = os.path.join(out_dir, 'dec-30_rgba_ndvi.png')
                    if vg_idx == 'NDVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'RVI':
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"
                    elif vg_idx == 'NIR':
                        vg = "https://user-images.githubusercontent.com/65748116/230503703-42e5b96e-5eb7-40c9-9674-b7420e0bdb2c.png"


            with row1_col1:

                op = st.slider('Opacity', 0.0, 1.0, 0.7, 0.1)
                m = display_map((33.67,73.13), 15, geo, dem, "DEM", vg, isDetected, op)
                m.to_streamlit(width=width, height=height)



        else:
            with row1_col1:
                m = leafmap.Map()
                st.pydeck_chart(m)



