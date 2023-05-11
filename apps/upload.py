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

# @st.cache(ttl=24*60*60)
def display_map(center, zoom, ndvi_json, health_json, orthomosaic, layer_title, legend_url, coords, detected=False, opacity=0.7):
    
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
        map.add_geojson(ndvi_json, layer_name="NDVI Map")
    
    map.add_geojson(health_json, layer_name="Health Map")
    ImageOverlay(orthomosaic,
                coords,
                opacity=opacity, name=layer_title
                ).add_to(map)
    
    FloatImage(legend_url, bottom=30, left=90, width=10).add_to(map)

    return map 



def app():

    st.title("Upload Vector Data")

    row1_col1, row1_col2 = st.columns([2, 1])
    width = 950
    height = 600
    map_dir = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\images\\map"
    lgnd_dir = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\images\\legends"
    geojs = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\geojson\\ndvi"
    hs = "C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\geojson\\health_stats"
    isDetected = True


    with open('C:\\Users\\DC\\Documents\\MachVIS\\FYP\\farm-dashboard\\apps\\styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    with row1_col2:
        container = st.container()
        with container:
            date = st.selectbox(
                "Select a date", ["26-12-22", "20-01-23", "24-02-23", "20-04-23"], index=1
            )

            vg_idx = st.radio(
                "Select a Vegetation Index",
                ('NDVI', 'SAVI')
            )

            # Display the chart using Streamlit
            fig = display_healthy_region()
            st.altair_chart(fig, use_container_width=True)




        # container = st.container()

        if date or vg_idx:
            # geojson = os.path.join(map_dir, 'ndvi.json')
            if date:
                if date == "26-12-22":
                    # dem = os.path.join(map_dir, 'ndvi/26_dec.png')
                    geo = os.path.join(geojs, '26_dec.json')
                    health = os.path.join(hs, 'health_stat_26_dec.json')
                    coords = [[33.672652308289614,73.12770497102615], [33.67436783460362,73.1307913403036]]
                    ndvi = 0.01
                    savi = 0.02
                    h_area = "5.22 Acres"
                    i_area = "1.55 Acres"
                    ph_stg = 'Tillering'
                    if vg_idx == 'NDVI':
                        dem = os.path.join(map_dir, 'ndvi/26_dec.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'SAVI':
                        dem = os.path.join(map_dir, 'savi/26_dec.png')
                        # geo = os.path.join(geojs, '20_jan.geojson')
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"

                elif date == "20-01-23":
                    # dem = os.path.join(map_dir, 'dec-26_rgba_ndvi.png')
                    # geo = os.path.join(geojs, '26.json')
                    geo = os.path.join(geojs, '20_jan.geojson')
                    health = os.path.join(hs, 'health_stat_20_jan.json')
                    coords = [[33.67373853226241, 73.1275590957505], [33.67529399233269, 73.130218601282]]
                    ndvi = 0.25
                    savi = 0.03
                    h_area = "4.06 Acres"
                    i_area = "4.32 Acres"
                    ph_stg = 'Tillering'                    
                    if vg_idx == 'NDVI':
                        dem = os.path.join(map_dir, 'ndvi/20_jan.png')
                        
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'SAVI':
                        dem = os.path.join(map_dir, 'savi/20_jan.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"
                  
                elif date == "24-02-23":
                    # dem = os.path.join(map_dir, 'dec-30_rgba_ndvi.png')
                    # geo = os.path.join(geojs, '26.json')
                    geo = os.path.join(geojs, '24_feb.geojson')
                    health = os.path.join(hs, 'health_stat_24_feb.json')
                    coords = [[33.67373853226241, 73.1275590957505], [33.67529399233269, 73.130218601282]]
                    ndvi = 0.5
                    savi = 0.5
                    h_area = "8.24 Acres"
                    i_area = "0.998 Acres"
                    ph_stg = 'Tillering'                    
                    if vg_idx == 'NDVI':
                        dem = os.path.join(map_dir, 'ndvi/24_feb.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'SAVI':
                        geo = os.path.join(hs, 'health_stat_24_feb')
                        dem = os.path.join(map_dir, 'savi/24_feb.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"

                elif date == "20-04-23":
                    # dem = os.path.join(map_dir, 'dec-30_rgba_ndvi.png')
                    # geo = os.path.join(geojs, '26.json')
                    geo = os.path.join(geojs, '20_apr.geojson')
                    health = os.path.join(hs, 'health_stat_20_apr.json')
                    coords = [[33.67373853226241, 73.1275590957505], [33.67529399233269, 73.130218601282]]
                    ndvi = 0.17
                    savi = 0.25
                    h_area = "5.83 Acres"
                    i_area = "2.41 Acres"
                    ph_stg = 'Tillering'
                    if vg_idx == 'NDVI':
                        dem = os.path.join(map_dir, 'ndvi/20_apr.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503462-174267ad-d850-41f7-afc3-b68ae9cd9e18.png"
                    elif vg_idx == 'SAVI':
                        dem = os.path.join(map_dir, 'savi/20_apr.png')
                        vg = "https://user-images.githubusercontent.com/65748116/230503711-e11d3019-a17b-4ab4-a217-924624ba7af4.png"


            with row1_col1:

                op = st.slider('Opacity', 0.0, 1.0, 0.7, 0.1)
                m = display_map((33.67,73.13), 15, geo, health, dem, "DEM", vg, coords, isDetected, op)
                print(m.get_bounds())
                print(m.location)
                m.to_streamlit(width=width, height=height)
                st.markdown("# **Analysis**")
                st.write(":seedling: Average NDVI:",ndvi)
                st.write(":leaves: Average SAVI: ",savi)
                st.write(":ear_of_rice: Phenological Stage: ",ph_stg)
                st.write(":blossom: Healthy Area: ",h_area)
                st.write(":ladybug: Infected Area: ",i_area)
                



        else:
            with row1_col1:
                m = leafmap.Map()
                st.pydeck_chart(m)



