import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, timelapse  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": timelapse.app, "title": "Timelapse", "icon": "map"},
    {"func": upload.app, "title": "Raster Viz", "icon": "map"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

# with st.sidebar:
#     selected = option_menu(
#         "Main Menu",
#         options=titles,
#         icons=icons,
#         menu_icon="cast",
#         default_index=default_index,
#     )

#     st.sidebar.title("About")
#     st.sidebar.info(
#         """
#         This web application is maintained by Asad Imtiaz. You can follow me on social media:
#             [GitHub](https://github.com/asadimtiazmalik) | [LinkedIn](https://www.linkedin.com/in/asadimtiazmalik).
        
#         Source code: <https://github.com/asadimtiazmalik/farm-dashboard>
#     """
#     )
selected = option_menu(
    None,
    options=titles,
    icons=icons,
    menu_icon="cast",
    orientation='horizontal',
    styles= {
        "container": {"padding": "0", "background-color": "#71c9c2", "border-radius": "5px"},
        "nav-link": {
            "font-size": "16px", 
            "text-align": "center", 
            "margin": "0 10px", 
            "padding": "10px",
            "color": "#f9f9f9",
            "border-bottom": "3px solid transparent",
            "--hover-color": "#9da4fa",
            "--selected-color": "#5590ed",

        },
        "nav-link:hover": {
            "background-color": "transparent",
            "border-bottom": "3px solid var(--hover-color)",
            "text-shadow": "0px 0px 5px #fff",
        },
        "nav-link-selected": {
            "background-color": "transparent",
            "border-bottom": "3px solid var(--selected-color)",
        },
    },
    default_index=0,
)

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
