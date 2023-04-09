import os
import geopandas as gpd
import streamlit as st
import os  
import leafmap.foliumap as leafmap
from folium.plugins import FloatImage
from folium.raster_layers import ImageOverlay
# import geopandas as gpd
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

            # if date == "23-12-23":
            #     dem_23 = os.path.join(out_dir, 'dec-16_rgba_ndvi.png')
            # elif date == "26-12-23":
            #     dem_26 = os.path.join(out_dir, 'dec-26_rgba_ndvi.png')
            # elif date == "30-12-23":
            #     dem_30 = os.path.join(out_dir, 'dec-30_rgba_ndvi.png')

            vg_idx = st.radio(
                "Select a Vegetation Index",
                ('NDVI', 'RVI', 'NIR')
            )

            # Define the data for the donut chart
            source = pd.DataFrame({"category": ["Healthy Area", "Infected Area", "Out of bounds"], "area in Acres": [5.22, 1.55, 2.74]})

            fig = alt.Chart(source).mark_arc(innerRadius=50).encode(
                theta=alt.Theta(field="area in Acres", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
                opacity = alt.value(0.6),
            )
            # Display the chart using Streamlit
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
                # file_path = save_uploaded_file(data, data.name)
                # file_path = dem_26
                # layer_name = os.path.splitext(data.name)[0]
            # elif vg_idx:
            #     fp=""
            #     # file_path = url
            #     # layer_name = url.split("/")[-1].split(".")[0]

            with row1_col1:
                # if file_path.lower().endswith(".kml"):
                #     gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
                #     gdf = gpd.read_file(file_path, driver="KML")
                # else:
                #     gdf = gpd.read_file(file_path)
                # lon, lat = leafmap.gdf_centroid(gdf)
                # if backend == "pydeck":

                #     column_names = gdf.columns.values.tolist()
                #     random_column = None
                #     with container:
                #         random_color = st.checkbox("Apply random colors", True)
                #         if random_color:
                #             random_column = st.selectbox(
                #                 "Select a column to apply random colors", column_names
                #             )

                m = leafmap.Map(center = (33.67,73.13), zoom=15)
                m.add_tile_layer(
                url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
                name="Google Satellite",
                attribution="Google",
                )

                # m.add_raster(dem_26, colormap='terrain', layer_name='DEM-26')
                if isDetected:
                    m.add_geojson(geo, layer_name="Health Indicator")
                op = st.slider('Opacity', 0.0, 1.0, 0.7, 0.1)
                ImageOverlay(dem,
                            [[33.672652308289614,73.12770497102615], [33.67436783460362,73.1307913403036]],
                            opacity=op, name='DEM'
                            ).add_to(m)
                
                FloatImage(vg, bottom=30, left=90, width=10).add_to(m)

                m.to_streamlit(width=width, height=height)


        else:
            with row1_col1:
                m = leafmap.Map()
                st.pydeck_chart(m)
                # out_dir = "C:\\Users\\DC\\Documents\\pix4d\\dec-26\\4_index\\indices\\ndvi"
                # dem_26 = os.path.join(out_dir, 'dec-26_rgba_ndvi.png')
                # geojson = os.path.join(out_dir, 'ndvi.json')



